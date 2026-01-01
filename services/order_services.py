from extensions import db
from models.user import User
from models.cart import CartItem
from models.product import Product
from models.order import Order, OrderItem

class OrderService:
    
    @staticmethod
    def place_order(email):
        user=User.query.filter_by(email=email).first()
        cart_items = CartItem.query.filter_by(user_id=user.id).all()
        if not cart_items:
            raise ValueError("Cart is empty")

        total_price = 0
        order_items_to_create = []

        try:
            # 1. Validate all items and calculate total
            for item in cart_items:
                product = item.product # Relationship from model
                
                if product.stock < item.quantity:
                    raise ValueError(f"Insufficient stock for {product.name}")

                # Update stock
                product.stock -= item.quantity
                
                # Calculate price
                item_total = product.price * item.quantity
                total_price += item_total

                # Prepare OrderItem record (snapshot current price)
                order_item = OrderItem(
                    product_id=product.id,
                    quantity=item.quantity,
                    price_at_purchase=product.price
                )
                order_items_to_create.append(order_item)

            # 2. Create the main Order record
            new_order = Order(user_id=user.id, total_price=total_price)
            db.session.add(new_order)
            db.session.flush() # Gets the order.id before committing

            # 3. Link items to order and add to session
            for oi in order_items_to_create:
                oi.order_id = new_order.id
                db.session.add(oi)

            # 4. Clear the cart
            CartItem.query.filter_by(user_id=user.id).delete()

            # 5. Commit everything to the database
            db.session.commit()

            return {
                "order_id": new_order.id,
                "total": total_price,
                "status": "Success"
            }

        except Exception as e:
            db.session.rollback() # Undo everything if any error occurs
            raise e