from flask import Blueprint
from views.category_views import CategoryListAPI, CategoryDetailAPI

category_bp = Blueprint('categories', __name__)

# GET /categories - List all
# POST /categories - Create new
category_bp.add_url_rule(
    '',
    view_func=CategoryListAPI.as_view('category_list'),
    methods=['GET', 'POST']
)

# GET /categories/<id> - Get single
# DELETE /categories/<id> - Delete
category_bp.add_url_rule(
    '/<int:id>',
    view_func=CategoryDetailAPI.as_view('category_detail'),
    methods=['GET', 'PATCH', 'DELETE']
)
