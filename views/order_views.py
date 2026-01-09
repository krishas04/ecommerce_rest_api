from flask.views import MethodView
from flask import jsonify, g, current_app
from middleware.auth_middleware import token_required
from services.order_services import OrderService
from schemas.order_schema import orders_schema, order_schema
from views.base_api import BaseAPI


class OrderListAPI(BaseAPI):
    
    @token_required
    def get(self):
        try:
            user_orders = OrderService.get_user_orders(g.user_email)
            
            return jsonify(orders_schema.dump(user_orders)), 200
            
        except Exception as e:
            current_app.logger.error(f"Fetch orders failed: {e}")
            return self.error_response(str(e), 500)
    
    @token_required
    def post(self):
        try:
            new_order = OrderService.place_order(g.user_email)
            
            return jsonify({
                "status": "success",
                "message": "Order placed successfully",
                "order": order_schema.dump(new_order)
            }), 201
            
        except ValueError as e:
            return jsonify({
                "status": "error",
                "message": str(e)
            }), 400
        except Exception as e:
            current_app.logger.error(f"Order placement failed: {e}")
            return jsonify({
                "status": "error",
                "message": "An unexpected error occurred."
            }), 500


class OrderDetailAPI(BaseAPI):
    
    @token_required
    def get(self, id):
        try:
            # Get order by ID
            order = OrderService.get_by_id(id)
            if not order:
                return self.error_response("Order not found", 404)
            
            return jsonify(order_schema.dump(order)), 200
            
        except Exception as e:
            return self.error_response(str(e), 500)


