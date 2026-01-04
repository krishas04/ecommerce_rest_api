from flask.views import MethodView
from flask import jsonify, g, current_app
from middleware.auth_middleware import token_required
from services.order_services import OrderService
from schemas.order_schema import orders_schema, order_schema
from views.base_api import BaseAPI


class OrderListAPI(BaseAPI):
    """Handle order collection endpoint"""
    
    @token_required
    def get(self):
        """GET /orders - Get logged-in user's orders"""
        try:
            # Get all orders for authenticated user
            user_orders = OrderService.get_user_orders(g.user_email)
            
            return jsonify(orders_schema.dump(user_orders)), 200
            
        except Exception as e:
            current_app.logger.error(f"Fetch orders failed: {e}")
            return self.error_response(str(e), 500)
    
    @token_required
    def post(self):
        """POST /orders - Place order from user's cart"""
        try:
            # Place order for authenticated user
            new_order = OrderService.place_order(g.user_email)
            
            # Return 201 Created with order details
            return jsonify({
                "status": "success",
                "message": "Order placed successfully",
                "order": order_schema.dump(new_order)
            }), 201
            
        except ValueError as e:
            # Business logic error (empty cart, out of stock, etc)
            return jsonify({
                "status": "error",
                "message": str(e)
            }), 400
        except Exception as e:
            # Unexpected error
            current_app.logger.error(f"Order placement failed: {e}")
            return jsonify({
                "status": "error",
                "message": "An unexpected error occurred."
            }), 500


class OrderDetailAPI(BaseAPI):
    """Handle single order endpoint """
    
    @token_required
    def get(self, id):
        """GET /orders/<id> - Get order details"""
        try:
            # Get order by ID
            order = OrderService.get_by_id(id)
            if not order:
                return self.error_response("Order not found", 404)
            
            return jsonify(order_schema.dump(order)), 200
            
        except Exception as e:
            return self.error_response(str(e), 500)


