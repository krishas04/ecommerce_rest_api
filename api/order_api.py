from flask import Blueprint
from views.order_views import OrderListAPI, OrderDetailAPI

order_bp = Blueprint('orders', __name__)

order_bp.add_url_rule(
    '',
    view_func=OrderListAPI.as_view('order_list'),
    methods=['GET', 'POST']
)

order_bp.add_url_rule(
    '/<id>',
    view_func=OrderDetailAPI.as_view('order_detail'),
    methods=['GET']
)