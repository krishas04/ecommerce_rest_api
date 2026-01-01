from flask import Blueprint, g, jsonify
from services.order_services import OrderService
from middleware.auth_middleware import token_required

# Create the Blueprint
order_bp = Blueprint('orders', __name__)

@order_bp.route('', methods=['POST'])
@token_required
def create_order():
    """
    REST Endpoint: POST /orders
    Action: Converts the current user's cart into a permanent order.
    """
    try:
        # g.user_email is populated by the @token_required decorator
        new_order = OrderService.place_order(g.user_email)
        
        # Return 201 Created (Standard for successful POST resource creation)
        return jsonify({
            "status": "success",
            "message": "Order placed successfully",
            "order": new_order
        }), 201

    except ValueError as e:
        # Standard REST: 400 Bad Request for business logic errors 
        # (e.g., empty cart or out of stock)
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400
    
    except Exception as e:
        # Standard REST: 500 Internal Server Error for unexpected crashes
        return jsonify({
            "status": "error",
            "message": "An unexpected error occurred."
        }), 500

@order_bp.route('', methods=['GET'])
@token_required
def get_my_orders():
    """
    REST Endpoint: GET /orders
    Action: Retrieves all orders for the logged-in user.
    """
    # Logic: Filter OrderService.orders for the current user
    user_orders = [o for o in OrderService.orders if o["user"] == g.user_email]
    return jsonify(user_orders), 200