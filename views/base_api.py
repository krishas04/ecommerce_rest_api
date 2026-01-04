from flask.views import MethodView
from flask import jsonify

class BaseAPI(MethodView):
    init_every_request = False  # Important: initialize once, reuse for all requests
    
    def error_response(self, message, code=400):
        """Reusable error handler - use instead of jsonify({"error": ...})"""
        return jsonify({"error": message}), code

    def success_response(self, data, code=200):
        """Reusable success handler"""
        return jsonify(data), code