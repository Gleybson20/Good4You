# app/routes/chat.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.mock_services import gerar_resposta, buscar_produtos  # Usando os mocks

router = APIRouter()

class ChatRequest(BaseModel):
    mensagem: str
    contexto: list = []

class ChatResponse(BaseModel):
    resposta: str
    produtos: list

@router.post("/", response_model=ChatResponse)
async def chat_interativo(body: ChatRequest):
    """
    Rota para interagir com o chatbot, gerar respostas e buscar produtos simulados.
    """
    try:
        # Gerando a resposta mockada para a mensagem do usuário
        resposta_ia = gerar_resposta(body.mensagem, body.contexto)  
        
        # Buscando produtos com base na resposta da NutriAI (mockada)
        produtos_sugeridos = buscar_produtos(resposta_ia)  
        
        return ChatResponse(resposta=resposta_ia, produtos=produtos_sugeridos)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
