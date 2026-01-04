from flask.views import MethodView
from flask import jsonify, request, g
from middleware.auth_middleware import token_required
from services.cart_services import CartService
from schemas.cart_schema import cart_items_schema, cart_item_schema
from views.base_api import BaseAPI


class CartListAPI(BaseAPI):
    """Handle cart collection endpoint"""
    @token_required
    def get(self):
        """GET /cart - Get logged-in user's cart items"""
        try:
            # Get cart items for authenticated user
            # g.user_email is set by @token_required middleware
            items = CartService.get_cart(g.user_email)
            
            return jsonify(cart_items_schema.dump(items)), 200
            
        except Exception as e:
            return self.error_response(str(e), 500)
    
    @token_required
    def post(self):
        """POST /cart - Add item to user's cart"""
        try:
            # Get product_id and quantity from request body
            data = request.get_json()
            
            # Add to cart for authenticated user
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
        """DELETE /cart - Clear all items from user's cart"""
        try:
            # Clear entire cart for authenticated user
            CartService.clear_cart(g.user_email)
            
            # Return 204 No Content
            return "", 204
            
        except Exception as e:
            return self.error_response(str(e))


class CartItemAPI(BaseAPI):
    """Handle single cart item endpoint"""
    @token_required
    def patch(self, id):
        """PATCH /cart/<id> - Update quantity of cart item"""
        try:
            # Get new quantity from request body
            data = request.get_json()
            quantity = data.get('quantity')
            
            if not quantity:
                return self.error_response("quantity field is required")
            
            # Update quantity in cart
            updated = CartService.update_cart_item(g.user_email, id, quantity)
            
            if not updated:
                return self.error_response("Cart item not found", 404)
            
            return jsonify(cart_item_schema.dump(updated)), 200
            
        except Exception as e:
            return self.error_response(str(e))
    
    @token_required
    def delete(self, id):
        """DELETE /cart/<id> - Remove item from cart"""
        try:
            # Remove specific item from cart
            CartService.remove_from_cart(g.user_email, id)
            
            # Return 204 No Content
            return "", 204
            
        except Exception as e:
            return self.error_response(str(e))