from flask import Blueprint
from views.cart_views import CartListAPI, CartItemAPI

cart_bp = Blueprint('cart', __name__)

cart_bp.add_url_rule(
    '',
    view_func=CartListAPI.as_view('cart_list'),
    methods=['GET', 'POST', 'DELETE']
)

cart_bp.add_url_rule(
    '/<int:id>',
    view_func=CartItemAPI.as_view('cart_item'),
    methods=['PATCH', 'DELETE']
)

