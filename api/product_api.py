from flask import Blueprint, request, jsonify
from services.product_services import ProductService
from schemas.product_schema import ProductSchema, product_schema, products_schema
from middleware.auth_middleware import token_required
from marshmallow import ValidationError

product_bp = Blueprint('products', __name__)

@product_bp.route('', methods=['GET'])
def list_products():
    # it receives Sqlalchemy objects
    products=ProductService.lists_products()
    #dump() converts these objects into JSON
    return jsonify(products_schema.dump(products)), 200

@product_bp.route('', methods=['POST'])
@token_required
def add_product():
    try:
        data = product_schema.load(request.get_json())
        result = ProductService.add_product(
            data.id, data.name, data.price,data.stock,data.category_id
        )
        return jsonify(result), 201
    except ValidationError as e:
        return jsonify(e.messages), 400

@product_bp.route('/<product_id>', methods=['GET'])
def get_product(product_id):
    product = ProductService.get_product(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product_schema.dump(product)), 200


