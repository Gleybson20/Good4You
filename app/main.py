# app/main.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware  # Para habilitar CORS
from fastapi.staticfiles import StaticFiles  # Para servir arquivos estáticos
import os
from dotenv import load_dotenv
from app.BD.Database import init_db  # Função para criar as tabelas
from app.services.database_services import adicionar_categoria, adicionar_produto  # Funções para manipulação de dados
from app.BD.Database import SessionLocal
from app.BD.models import Categoria, Produto

# Carregar variáveis de ambiente
load_dotenv()

# Inicializando o FastAPI
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

# Inicializar o banco de dados e adicionar produtos/categorias iniciais
def init():
    # Inicializar o banco de dados (criar as tabelas, se não existirem)
    init_db()

    # Criar categorias e produtos iniciais (caso ainda não existam no banco)
    db = SessionLocal()

    # Adicionar categorias iniciais
    if not db.query(Categoria).filter(Categoria.nome == "Proteínas").first():
        adicionar_categoria(db, "Proteínas")
    if not db.query(Categoria).filter(Categoria.nome == "Vegetais").first():
        adicionar_categoria(db, "Vegetais")
    
    # Adicionar alguns produtos iniciais (caso não existam)
    if not db.query(Produto).first():  # Verifica se existem produtos
        categoria_proteinas = db.query(Categoria).filter(Categoria.nome == "Proteínas").first()
        categoria_vegetais = db.query(Categoria).filter(Categoria.nome == "Vegetais").first()
        
        # Exemplo de produtos iniciais
        adicionar_produto(db, "Peito de Frango", "Frango rico em proteínas", 10.0, 200.0, 40.0, 0.0, 5.0, categoria_proteinas.id)
        adicionar_produto(db, "Brócolis", "Vegetal rico em fibras e vitaminas", 5.0, 50.0, 4.0, 10.0, 1.0, categoria_vegetais.id)

    db.close()

# Rota inicial para carregar a UI do Swagger
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>NutriAI Chatbot</title>
        </head>
        <body>
            <h1>Bem-vindo ao NutriAI Chatbot!</h1>
            <p>Acesse <a href="/docs">aqui</a> para ver a documentação da API (Swagger UI).</p>
        </body>
    </html>
"""

# Inicializando o banco de dados e adicionando produtos/categorias iniciais
init()

# Incluindo as rotas
from app.routes import chat, products

app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(products.router, prefix="/products", tags=["Produtos"])

# Endpoint de teste
@app.get("/status")
async def status():
    return {"status": "API funcionando corretamente"}
