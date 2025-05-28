# Consultas à Shopify 

from fastapi import APIRouter, Query, HTTPException
from typing import List
from app.services.shopify_services import buscar_produtos

router = APIRouter()

@router.get("/")
async def buscar_produtos_endpoint(termo: str = Query(..., description="Termo para buscar produtos na Shopify")):
    try:
        produtos = buscar_produtos(termo)
        return {"produtos": produtos}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
