from flask.views import MethodView
from flask import jsonify, request
from marshmallow import ValidationError
from services.auth_services import AuthService
from schemas.user_schema import user_schema
from views.base_api import BaseAPI


class RegisterAPI(BaseAPI):
    def post(self):
        """POST /auth/register - Create new user account"""
        try:
            # Validate input data using schema
            user_data = user_schema.load(request.get_json())
            
            # Call service to register user
            result = AuthService.register(user_data.email, user_data.password)
            
            # Return 201 Created
            return jsonify(result), 201
            
        except ValidationError as e:
            # Schema validation error (e.g., invalid email format)
            return jsonify(e.messages), 400
        except Exception as e:
            # Other errors (e.g., user already exists)
            return self.error_response(str(e))


class LoginAPI(BaseAPI):
    def post(self):
        """POST /auth/login - Authenticate user and get JWT token"""
        try:
            data = request.get_json()
            
            # Call service to authenticate and get token
            result = AuthService.login(data['email'], data['password'])
            
            # Return 200 OK with token
            return jsonify(result), 200
            
        except KeyError:
            # Missing email or password
            return self.error_response("Missing email or password")
        except Exception as e:
            # Invalid credentials
            return self.error_response(str(e), 401)