from flask import Blueprint
from views.product_views import ProductListAPI, ProductDetailAPI

product_bp = Blueprint('products', __name__)

# GET /products - List all
# POST /products - Create new
product_bp.add_url_rule(
    '',
    view_func=ProductListAPI.as_view('product_list'),
    methods=['GET', 'POST']
)

# GET /products/<id> - Get single
# PATCH /products/<id> - Update
# DELETE /products/<id> - Delete
product_bp.add_url_rule(
    '/<product_id>',
    view_func=ProductDetailAPI.as_view('product_detail'),
    methods=['GET', 'PATCH', 'DELETE']
)
