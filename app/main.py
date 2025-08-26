from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from app.BD.Database import init_db, db
from app.schemas.chat_schemas import ChatRequest, ChatResponse
from app.schemas.product_schema import ProductListResponse, Product
from app.services.openai.openai_api import chat_with_openai
from app.services.shopify.shopify_api import get_products

app = FastAPI()

# Inicializa o banco de dados
def init():
    init_db(app)

# Serve arquivos estáticos, como CSS, JS, imagens, etc.
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>Chatbot NutriAI - Loja Virtual</title>
            <link rel="stylesheet" href="/static/style.css">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css">
        </head>
        <body>
            <div class="main-container">
                <div class="wrapper">
                    <div class="title">Chatbot NutriAI</div>
                    <div class="box">
                        <!-- Mensagens dinâmicas serão adicionadas aqui -->
                    </div>
                    <div class="typing-area">
                        <div class="input-field">
                            <input type="text" id="user-input" placeholder="Digite sua dúvida" required onkeyup="checkEnter(event)">
                            <button onclick="sendMessage()">Enviar</button>
                        </div>
                    </div>
                </div>

                <div class="swagger-button-container">
                    <button onclick="window.location.href='/docs';" class="swagger-btn">
                        Acessar Documentação
                    </button>
                </div>
            </div>

            <script>
                function checkEnter(event) {
                    if (event.key === "Enter") {
                        sendMessage();
                    }
                }

                function sendMessage() {
                    const inputField = document.getElementById("user-input");
                    const userMessage = inputField.value.trim();
                    if (userMessage === "") return;

                    addMessage(userMessage, 'user');

                    fetch("http://127.0.0.1:8000/chat/", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            mensagem: userMessage,
                            contexto: []  // Pode ser estendido para incluir mensagens anteriores, se necessário
                        })
                    })
                    .then(response => response.json())
                    .then(data => {
                        const botResponse = data.resposta;
                        addMessage(botResponse, 'bot');
                        if (data.produtos && data.produtos.length > 0) {
                            addMessage("Aqui estão alguns produtos recomendados para você:", 'bot');
                            data.produtos.forEach(produto => {
                                addMessage(`${produto.title} - ID: ${produto.id}`, 'bot');
                            });
                        }
                    })
                    .catch(error => {
                        console.error('Erro ao enviar mensagem:', error);
                        addMessage("Desculpe, houve um erro ao processar sua solicitação.", 'bot');
                    });

                    inputField.value = "";
                    inputField.focus();
                }

                function addMessage(message, sender) {
                    const chatBox = document.querySelector(".box");
                    const messageElement = document.createElement("div");
                    messageElement.classList.add("item", sender);
                    messageElement.innerHTML = `
                        <div class="icon">
                            <i class="fa ${sender === 'user' ? 'fa-user' : 'fa-robot'}"></i>
                        </div>
                        <div class="msg">
                            <p>${message}</p>
                        </div>
                    `;
                    chatBox.appendChild(messageElement);
                    chatBox.scrollTop = chatBox.scrollHeight;
                }
            </script>
        </body>
    </html>
    """

@app.get("/products", response_model=ProductListResponse)
def get_products_route():
    """
    Rota para buscar todos os produtos da loja na Shopify
    """
    products = get_products()
    return {"produtos": [Product(id=prod['id'], title=prod['title']) for prod in products]}

@app.post("/chat", response_model=ChatResponse)
def chat_with_bot(chat_request: ChatRequest):
    """
    Rota para interação com o chatbot da OpenAI.
    A API espera um JSON com a mensagem do usuário e o contexto de conversa.
    """
    openai_response = chat_with_openai(
        messages=[{"role": "user", "content": chat_request.mensagem}],
        model="gpt-3.5-turbo",
        temperature=0.7,
        max_tokens=150
    )

    produtos_recomendados = get_products()

    return ChatResponse(
        resposta=openai_response,
        produtos=[{"id": prod['id'], "title": prod['title']} for prod in produtos_recomendados]
    )

if __name__ == "__main__":
    import uvicorn
    init()
    uvicorn.run(app, host="0.0.0.0", port=8000)
