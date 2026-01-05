from flask.views import MethodView
from flask import jsonify, request
from marshmallow import ValidationError
from services.auth_services import AuthService
from schemas.user_schema import user_schema
from views.base_api import BaseAPI


class RegisterAPI(BaseAPI):
    def post(self):
        try:
            user_data = user_schema.load(request.get_json())
            
            result = AuthService.register(user_data.email, user_data.password)
            
            return jsonify(result), 201
            
        except ValidationError as e:
            return jsonify(e.messages), 400
        except Exception as e:
            return self.error_response(str(e))


class LoginAPI(BaseAPI):
    def post(self):
        try:
            data = request.get_json()
            
            result = AuthService.login(data['email'], data['password'])
            
            return jsonify(result), 200
            
        except KeyError:
            return self.error_response("Missing email or password")
        except Exception as e:
            return self.error_response(str(e), 401)