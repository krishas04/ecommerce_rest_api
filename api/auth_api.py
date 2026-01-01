from flask import Blueprint, request, jsonify
from services.auth_services import AuthService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
        result = AuthService.register(data['email'], data['password'])
        return jsonify(result), 201
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