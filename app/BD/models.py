# app/BD/models.py

from app.BD.Database import db  # Importando db de database.py diretamente

class Product(db.Model):
    """Modelo de produto"""
    id = db.Column(db.Integer, primary_key=True)
    shopify_id = db.Column(db.String(255), unique=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

class Order(db.Model):
    """Modelo de pedido"""
    id = db.Column(db.Integer, primary_key=True)
    shopify_id = db.Column(db.String(255), unique=True, nullable=False)
    total_price = db.Column(db.Float)

class Customer(db.Model):
    """Modelo de cliente"""
    id = db.Column(db.Integer, primary_key=True)
    shopify_id = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True)
