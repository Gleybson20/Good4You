from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware  # Para habilitar CORS
from fastapi.staticfiles import StaticFiles  # Para servir arquivos estáticos
import os

app = FastAPI(
    title="Chatbot NutriAI + Shopify",
    description="API de integração entre NutriAI e Shopify para sugerir dietas personalizadas e produtos.",
    version="0.1.0",
    docs_url=None,  # Desliga o Swagger UI padrão
    redoc_url="/redoc",  # ReDoc, com um layout mais limpo
)

# Habilitando CORS (se você for acessar de uma interface diferente)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens, pode especificar as origens mais tarde
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

# Configurando para servir arquivos estáticos da pasta 'static'
app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "static")), name="static")

@app.get("/docs", response_class=HTMLResponse)
async def custom_swagger_ui_html():
    # Caminho para o arquivo HTML no diretório 'static'
    file_path = os.path.join(os.path.dirname(__file__), "static", "swagger_ui.html")
    
    # Verifica se o arquivo existe e retorna seu conteúdo
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return f.read()
    return "Documentação personalizada não encontrada."

# Incluindo as rotas
from app.routes import chat, products

app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(products.router, prefix="/products", tags=["Produtos"])

# Endpoint de teste
@app.get("/")
async def root():
    return {"message": "Bem-vindo à API do Chatbot!"}
