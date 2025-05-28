# Entrypoint do FastAPI

from fastapi import FastAPI
from app.routes import chat, products

app = FastAPI(
    title="Chatbot",
    description="Backend API para integração entre Nutri AI e Shopify",
    version="0.1.0",
)

app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(products.router, prefix="/products", tags=["Produtos"])

@app.get("/")
async def root():
    return {"message": "Bem-vindo à API do Chatbot!"}
