# app/services/dieta_services.py
from app.BD.models import Produto
from sqlalchemy.orm import Session

def gerar_dieta_usuario(usuario):
    dieta = []
    produtos_adequados = buscar_produtos_para_dieta(usuario.preferencias)

    for produto in produtos_adequados:
        if validar_produto_para_usuario(produto, usuario):
            dieta.append(produto)

    return dieta

def buscar_produtos_para_dieta(preferencias):
    produtos = Produto.query.filter(Produto.calorias <= preferencias["calorias_maxima"]).all()
    return produtos

def validar_produto_para_usuario(produto, usuario):
    return True  # Implementar lógica de validação
