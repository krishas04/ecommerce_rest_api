from flask import Blueprint, request, jsonify
from services.product_services import ProductService
from middleware.auth_middleware import token_required

product_bp = Blueprint('products', __name__)

@product_bp.route('', methods=['GET'])
def list_products():
    return jsonify(ProductService.lists_products()), 200

@product_bp.route('', methods=['POST'])
@token_required
def add_product():
    data = request.get_json()
    try:
        result = ProductService.add_product(
            data['product_id'], data['name'], data['price'], data['stock']
        )
        return jsonify(result), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@product_bp.route('/<product_id>', methods=['GET'])
def get_product(product_id):
    product = ProductService.get_product(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product), 200