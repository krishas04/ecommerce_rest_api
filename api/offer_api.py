from flask import Blueprint
from views.offer_views import OfferListAPI, OfferDetailAPI

offer_bp = Blueprint('offers', __name__)

offer_bp.add_url_rule(
    '',
    view_func=OfferListAPI.as_view('offer_list'),
    methods=['GET', 'POST']
)

offer_bp.add_url_rule(
    '/<int:id>',
    view_func=OfferDetailAPI.as_view('offer_detail'),
    methods=['GET', 'PATCH', 'DELETE']
)

