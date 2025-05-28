 # Conversa com Nutri AI

from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel
from app.services.openai_services import gerar_resposta
from app.services.shopify_services import buscar_produtos

router = APIRouter()

class ChatRequest(BaseModel):
    mensagem: str
    contexto: list = []

class ChatResponse(BaseModel):
    resposta: str
    produtos: list

@router.post("/", response_model=ChatResponse)
async def chat_interativo(body: ChatRequest):
    try:
        resposta_ia = gerar_resposta(body.mensagem, body.contexto)
        produtos_sugeridos = buscar_produtos(resposta_ia)
        return ChatResponse(resposta=resposta_ia, produtos=produtos_sugeridos)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
