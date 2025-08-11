# app/services/shopify_services.py
import requests

SHOPIFY_API_KEY = 'sua-chave-api'
SHOPIFY_STORE_URL = 'sua-loja.myshopify.com'
SHOPIFY_API_VERSION = '2025-01'


def buscar_produtos_nutricionais(termo: str):
    """
    Função para buscar produtos na Shopify e extrair informações nutricionais.
    """
    url = f"https://{SHOPIFY_STORE_URL}/admin/api/{SHOPIFY_API_VERSION}/products.json"
    params = {"title": termo}  # Buscando produtos com o título semelhante ao termo
    headers = {"X-Shopify-Access-Token": SHOPIFY_API_KEY}

    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        produtos = response.json()["products"]
        detalhes_produtos = []

        for produto in produtos:
            descricao = produto.get("body_html", "Sem descrição disponível")
            detalhes_produtos.append({
                "nome": produto["title"],
                "preco": float(produto["variants"][0]["price"]),
                "descricao": descricao,
                "imagem": produto["images"][0]["src"] if produto.get("images") else "Sem imagem disponível",
                "calorias": extrair_calorias(descricao),  # Função para extrair calorias da descrição
                "proteinas": extrair_macros(descricao, "proteina"),
                "carboidratos": extrair_macros(descricao, "carboidrato"),
                "gorduras": extrair_macros(descricao, "gordura")
            })

        return detalhes_produtos
    else:
        raise Exception(f"Erro ao buscar produtos: {response.status_code}")

def extrair_calorias(descricao):
    # Implementar lógica para buscar calorias na descrição do produto
    pass

def extrair_macros(descricao, tipo):
    # Similar à função acima, para extrair a quantidade de proteínas, carboidratos ou gorduras da descrição
    pass
