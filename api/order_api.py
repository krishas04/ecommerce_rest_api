from flask import Blueprint, g, jsonify
from services.order_services import OrderService
from middleware.auth_middleware import token_required
from schemas.order_schema import order_schema, orders_schema
import logging 
from flask import current_app

# Create the Blueprint
order_bp = Blueprint('orders', __name__)

@order_bp.route('', methods=['POST'])
@token_required
def create_order():
    try:
        
        new_order = OrderService.place_order(g.user_email)
        
        # Return 201 Created (Standard for successful POST resource creation)
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
            "message": "Internal error"
        }), 500

@order_bp.route('', methods=['GET'])
@token_required
def get_my_orders():
    user_orders = OrderService.get_user_orders(g.user_email)
    return jsonify(order_schema.dump(user_orders)), 200