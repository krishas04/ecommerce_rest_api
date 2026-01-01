from flask import Blueprint, request, jsonify, g
from services.cart_services import CartService
from middleware.auth_middleware import token_required

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('', methods=['GET'])
@token_required
def get_cart():
    # Email comes from the token, not the URL or body
    return jsonify(CartService.get_cart(g.user_email)), 200

@cart_bp.route('', methods=['POST'])
@token_required
def add_to_cart():
    data = request.get_json()
    try:
        result = CartService.add_to_cart(g.user_email, data['product_id'], data['quantity'])
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400