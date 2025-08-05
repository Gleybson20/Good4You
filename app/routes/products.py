# app/routes/products.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.BD.Database import SessionLocal
from app.services.database_services import adicionar_produto, buscar_produtos

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/produtos/")
async def criar_produto(nome: str, descricao: str, preco: float, calorias: float, 
                        proteinas: float, carboidratos: float, gorduras: float, categoria_id: int, 
                        db: Session = Depends(get_db)):
    produto = adicionar_produto(db, nome, descricao, preco, calorias, proteinas, carboidratos, gorduras, categoria_id)
    return produto

@router.get("/produtos/")
async def buscar_produtos_endpoint(termo: str, db: Session = Depends(get_db)):
    produtos = buscar_produtos(db, termo)
    return {"produtos": produtos}
