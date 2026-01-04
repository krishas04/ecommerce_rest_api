from flask import Blueprint
from views.order_views import OrderListAPI, OrderDetailAPI

order_bp = Blueprint('orders', __name__)

# GET /orders - Get user's orders
# POST /orders - Place new order
order_bp.add_url_rule(
    '',
    view_func=OrderListAPI.as_view('order_list'),
    methods=['GET', 'POST']
)

# GET /orders/<id> - Get order details
order_bp.add_url_rule(
    '/<id>',
    view_func=OrderDetailAPI.as_view('order_detail'),
    methods=['GET']
)