# app/services/database_services.py
from sqlalchemy.orm import Session
from app.BD.models import Produto, Categoria, Conversa, Usuario

def adicionar_categoria(db: Session, nome: str):
    categoria = Categoria(nome=nome)
    db.add(categoria)
    db.commit()
    db.refresh(categoria)
    return categoria

def adicionar_produto(db: Session, nome: str, descricao: str, preco: float, calorias: float, 
                      proteinas: float, carboidratos: float, gorduras: float, categoria_id: int):
    produto = Produto(nome=nome, descricao=descricao, preco=preco, calorias=calorias,
                      proteinas=proteinas, carboidratos=carboidratos, gorduras=gorduras, 
                      categoria_id=categoria_id)
    db.add(produto)
    db.commit()
    db.refresh(produto)
    return produto

def buscar_produtos_por_categoria(db: Session, categoria_nome: str):
    return db.query(Produto).join(Categoria).filter(Categoria.nome == categoria_nome).all()

def buscar_produtos(db: Session, termo: str):
    return db.query(Produto).filter(Produto.nome.contains(termo)).all()

def buscar_historico_conversas(db: Session, usuario_id: int):
    return db.query(Conversa).filter(Conversa.usuario_id == usuario_id).all()
