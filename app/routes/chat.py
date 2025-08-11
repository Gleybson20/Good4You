# app/routes/chat.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.openai.openai_services import gerar_resposta
from app.services.shopify.shopify_services import buscar_produtos_nutricionais  # Se necessário

router = APIRouter()

class ChatRequest(BaseModel):
    mensagem: str
    contexto: list = []
    usuario_id: int  # Para associar a conversa a um usuário específico

class ChatResponse(BaseModel):
    resposta: str
    dieta: list  # Dieta gerada para o usuário

@router.post("/", response_model=ChatResponse)
async def chat_interativo(body: ChatRequest):
    try:
        resposta_ia = gerar_resposta(body.mensagem, body.contexto)
        produtos_sugeridos = buscar_produtos_nutricionais(resposta_ia)

        return ChatResponse(resposta=resposta_ia)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
