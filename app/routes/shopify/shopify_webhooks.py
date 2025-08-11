from flask import Blueprint, request, jsonify
import hmac
import hashlib
import json

shopify_webhooks = Blueprint('shopify_webhooks', __name__)

def verify_hmac(data, hmac_header):
    secret = "your_shopify_secret"
    computed_hmac = hmac.new(secret.encode('utf-8'), data, hashlib.sha256).hexdigest()
    return computed_hmac == hmac_header

@shopify_webhooks.route('/webhook', methods=['POST'])
def receive_webhook():
    data = request.data
    hmac_header = request.headers.get('X-Shopify-Hmac-Sha256')
    if not verify_hmac(data, hmac_header):
        return jsonify({"error": "Unauthorized"}), 403

    webhook_data = json.loads(data)
    topic = request.headers.get('X-Shopify-Topic')

    # Dependendo do tipo de webhook, atualize os dados
    if topic == 'products/update':
        # Atualize ou crie produto no banco
        pass
    elif topic == 'orders/create':
        # Atualize ou crie pedido no banco
        pass
    
    return jsonify({"status": "success"}), 200
