from flask import Blueprint
from views.auth_views import RegisterAPI, LoginAPI

auth_bp = Blueprint('auth', __name__)

# POST /auth/register - Register new user
auth_bp.add_url_rule(
    '/register',
    view_func=RegisterAPI.as_view('register'),
    methods=['POST']
)

# POST /auth/login - Login user
auth_bp.add_url_rule(
    '/login',
    view_func=LoginAPI.as_view('login'),
    methods=['POST']
)