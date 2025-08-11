import requests
from app.utils.context_manager import log_error


SHOPIFY_SHOP_URL = "https://your-shop.myshopify.com/admin/api/2021-07"
SHOPIFY_ACCESS_TOKEN = "your_access_token"

def get_products():
    url = f"{SHOPIFY_SHOP_URL}/products.json"
    headers = {"X-Shopify-Access-Token": SHOPIFY_ACCESS_TOKEN}
    try:
        response = requests.get(url, headers=headers)
        return response.json()['products']
    except Exception as e:
        log_error(f"Error fetching products: {e}")
        return []

def update_product_in_db(product_data):
    # Aqui vamos adicionar a lógica de persistência dos dados no banco
    pass
