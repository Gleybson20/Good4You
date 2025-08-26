from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    """Inicializa o banco de dados no app FastAPI"""
    db.init_app(app)
