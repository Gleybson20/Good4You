# app/BD/models.py
from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.mutable import MutableDict  # Importa MutableDict para dados JSON mutáveis
from sqlalchemy.types import JSON  # Importa o tipo JSON
from app.BD.Database import Base  # Base precisa ser definido em outro arquivo

class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    produtos = relationship("Produto", back_populates="categoria")

class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(Text)
    preco = Column(Float)
    calorias = Column(Float)
    proteinas = Column(Float)
    carboidratos = Column(Float)
    gorduras = Column(Float)
    imagem_url = Column(String)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    categoria = relationship("Categoria", back_populates="produtos")

class Conversa(Base):
    __tablename__ = "conversas"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, index=True)
    mensagem = Column(Text)
    resposta = Column(Text)
    produtos_sugeridos = Column(JSON)  # Lista de produtos sugeridos armazenados como JSON
    timestamp = Column(Integer)  # Timestamp da conversa

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String, unique=True, index=True)
    preferencias = Column(MutableDict.as_mutable(JSON))  # Utiliza MutableDict para garantir mutabilidade
    objetivo_calorias = Column(Float)
    objetivo_proteinas = Column(Float)
