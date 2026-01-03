from extensions import db
from models.user import User
from models.cart import CartItem
from models.product import Product
from models.order import Order, OrderItem
import uuid

class OrderService:
    @staticmethod
    def place_order(email: str):
        # 1. Find the user
        user = User.query.filter_by(email=email).first()
        if not user:
            raise ValueError("User not found.")

        # 2. Get all cart items for this user
        cart_items = CartItem.query.filter_by(user_id=user.id).all()
        if not cart_items:
            raise ValueError("Cart is empty.")

        # 3. Validate stock
        for item in cart_items:
            if item.quantity > item.product.stock:
                raise ValueError(f"Not enough stock for {item.product.name}.")

        # 4. Create the order
        order = Order(
            id=str(uuid.uuid4()),   # UUID for order ID
            user_id=user.id,
            total_price=0.0
        )
        db.session.add(order)

        total_price = 0.0

        # 5. Create order items and update stock
        for item in cart_items:
            current_price=item.product.get_current_price()
            subtotal = item.quantity * current_price
            total_price += subtotal

            order_item = OrderItem(
                order_id=order.id,
                product_id=item.product_id,
                quantity=item.quantity,
                rate=current_price,
                price_at_purchase=item.quantity * current_price
            )
            db.session.add(order_item)

            # Reduce product stock
            item.product.stock -= item.quantity

            # Remove item from cart
            db.session.delete(item)

        # 6. Update order total and commit
        order.total_price = round(total_price, 2)
        db.session.commit()

        return order
