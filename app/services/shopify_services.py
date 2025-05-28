# Comunicação Shopify

import os
import requests

SHOPIFY_API_URL = os.getenv("SHOPIFY_API_URL")  # ex: https://yourstore.myshopify.com/admin/api/2023-01
SHOPIFY_API_TOKEN = os.getenv("SHOPIFY_API_TOKEN")

def buscar_produtos(texto: str) -> list:

    try:
        termos = extrair_ingredientes(texto)

        produtos = []
        headers = {
            "X-Shopify-Access-Token": SHOPIFY_API_TOKEN,
            "Content-Type": "application/json",
        }

        for termo in termos:
            url = f"{SHOPIFY_API_URL}/products.json?title={termo}"
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            produtos += response.json().get("products", [])

        return produtos
    
    except Exception as e:
        raise RuntimeError(f"Erro ao buscar produtos Shopify: {str(e)}")

def extrair_ingredientes(texto: str) -> list:

    palavras = set(p.lower() for p in texto.split() if len(p) > 3)
    return list(palavras)
