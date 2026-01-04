from flask import Blueprint
from views.cart_views import CartListAPI, CartItemAPI

cart_bp = Blueprint('cart', __name__)

# GET /cart - Get user's cart
# POST /cart - Add item to cart
# DELETE /cart - Clear cart
cart_bp.add_url_rule(
    '',
    view_func=CartListAPI.as_view('cart_list'),
    methods=['GET', 'POST', 'DELETE']
)

# PATCH /cart/<id> - Update item quantity
# DELETE /cart/<id> - Remove item
cart_bp.add_url_rule(
    '/<int:id>',
    view_func=CartItemAPI.as_view('cart_item'),
    methods=['PATCH', 'DELETE']
)

