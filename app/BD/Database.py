# app/BD/database.py

from flask_sqlalchemy import SQLAlchemy

# Instancia o objeto db (SQLAlchemy)
db = SQLAlchemy()

# Função para inicializar o banco de dados no aplicativo
def init_db(app):
    """Inicializa o banco de dados no app FastAPI"""
    db.init_app(app)
