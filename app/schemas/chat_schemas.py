# app/schemas/chat_schema.py
from pydantic import BaseModel
from typing import List

class ChatRequest(BaseModel):
    mensagem: str
    contexto: List[str] = []

class ChatResponse(BaseModel):
    resposta: str
    produtos: List[dict]