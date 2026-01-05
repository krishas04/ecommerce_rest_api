from flask.views import MethodView
from flask import jsonify

class BaseAPI(MethodView):
    init_every_request = False  # Important: initialize once, reuse for all requests
    
    def error_response(self, message, code=400):
        return jsonify({"error": message}), code

    def success_response(self, data, code=200):
        return jsonify({"success":data}), code