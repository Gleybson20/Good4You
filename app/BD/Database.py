from flask_sqlalchemy import SQLAlchemy

# Instância do banco de dados
db = SQLAlchemy()

# Função para configurar a base de dados
def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # ou outro banco
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
