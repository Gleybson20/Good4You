# app/BD/Database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"  # Exemplo com SQLite, mas pode usar PostgreSQL

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})  # Ajuste para SQLite
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Função para criar o banco de dados
def init_db():
    Base.metadata.create_all(bind=engine)
