from flask.views import MethodView
from flask import jsonify, request, g
from middleware.auth_middleware import token_required
from services.cart_services import CartService
from schemas.cart_schema import cart_items_schema, cart_item_schema
from views.base_api import BaseAPI


class CartListAPI(BaseAPI):
    @token_required
    def get(self):
        try:
            items = CartService.get_cart(g.user_email)
            
            return jsonify(cart_items_schema.dump(items)), 200
            
        except Exception as e:
            return self.error_response(str(e), 500)
    
    @token_required
    def post(self):
        try:
            data = request.get_json()
            
            result = CartService.add_to_cart(
                g.user_email,
                data['product_id'],
                data['quantity']
            )
            
            return jsonify(result), 200
            
        except KeyError as e:
            return self.error_response(f"Missing field: {str(e)}")
        except Exception as e:
            return self.error_response(str(e))
    
    @token_required
    def delete(self):
        try:
            CartService.clear_cart(g.user_email)
            
            return "", 204
            
        except Exception as e:
            return self.error_response(str(e))


class CartItemAPI(BaseAPI):
    @token_required
    def patch(self, id):
        try:
            data = request.get_json()
            quantity = data.get('quantity')
            
            if not quantity:
                return self.error_response("quantity field is required")
            
            updated = CartService.update_cart_item(g.user_email, id, quantity)
            
            if not updated:
                return self.error_response("Cart item not found", 404)
            
            return jsonify(cart_item_schema.dump(updated)), 200
            
        except Exception as e:
            return self.error_response(str(e))
    
    @token_required
    def delete(self, id):
        try:
            CartService.remove_from_cart(g.user_email, id)
            
            return "", 204
            
        except Exception as e:
            return self.error_response(str(e))