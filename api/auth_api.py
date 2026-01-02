from flask import Blueprint, request, jsonify
from services.auth_services import AuthService
from schemas.user_schema import user_schema
from marshmallow import ValidationError

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        user_data = user_schema.load(request.get_json())
        result = AuthService.register(user_data.email, user_data.password)
        return jsonify(result), 201
    except ValidationError as e:
        return jsonify(e.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        result = AuthService.login(data['email'], data['password'])
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401