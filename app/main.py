# app/main.py

from fastapi import FastAPI
from app.BD.Database import init_db  # Importando a função de inicialização do banco de dados

# Criando uma instância do FastAPI
app = FastAPI()

# Inicializa o banco de dados ao iniciar o servidor
@app.on_event("startup")
async def startup_event():
    from app.BD.Database import db
    init_db(app)  # Inicializa o banco de dados no FastAPI

# Rota para verificar se o servidor está funcionando
@app.get("/health")
async def health_check():
    return {"status": "Servidor funcionando"}
