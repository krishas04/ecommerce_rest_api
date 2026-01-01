from extensions import db
from models.cart import CartItem
from models.product import Product
from models.user import User

class CartService:
    # Simulated Database: { "email@example.com": [ {item1}, {item2} ] }
    carts = {}

    @staticmethod
    def add_to_cart(email, product_id, quantity):
         # 1. Find the user and product
        user = User.query.filter_by(email=email).first()
        product = Product.query.get(product_id)

        if not product:
            raise ValueError("Product not found.")
        if product.stock < quantity:
            raise ValueError("Not enough stock available.")

        # 2. Check if the item is already in the cart
        item = CartItem.query.filter_by(user_id=user.id, product_id=product_id).first()

        if item:
            item.quantity += quantity
        else:
         # 3. Create new cart item
            item = CartItem(user_id=user.id, product_id=product_id, quantity=quantity)
            db.session.add(item)

        db.session.commit()
        return {"message": "Cart updated"}


    @staticmethod
    def get_cart(email):
        user = User.query.filter_by(email=email).first()
        items = CartItem.query.filter_by(user_id=user.id).all()
        
        return [{
            "product_id": item.product_id,
            "name": item.product.name,
            "price": item.product.price,
            "quantity": item.quantity,
            "subtotal": item.product.price * item.quantity
        } for item in items]

    @staticmethod
    def clear_cart(email):
        user = User.query.filter_by(email=email).first()
        CartItem.query.filter_by(user_id=user.id).delete()
        db.session.commit()