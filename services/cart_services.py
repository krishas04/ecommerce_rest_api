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
        return {"message": "Added to cart"}


    @staticmethod
    def get_cart(email):
        user = User.query.filter_by(email=email).first()
        items = CartItem.query.filter_by(user_id=user.id).all()
        
        return items

    @staticmethod
    def clear_cart(email):
        user = User.query.filter_by(email=email).first()
        CartItem.query.filter_by(user_id=user.id).delete()
        db.session.commit()

    @staticmethod
    def get_cart_item(email, item_id):
        """
        Get specific cart item for user
        Returns: CartItem object or None
        """
        user = User.query.filter_by(email=email).first()
        if not user:
            return None
        
        item = CartItem.query.filter_by(
            id=item_id, 
            user_id=user.id
        ).first()
        
        return item
    
    @staticmethod
    def update_cart_item(email, item_id, quantity):
        """
        Update quantity of cart item
        Returns: Updated CartItem object or None
        """
        user = User.query.filter_by(email=email).first()
        if not user:
            return None
        
        item = CartItem.query.filter_by(
            id=item_id, 
            user_id=user.id
        ).first()
        
        if item:
            # Check stock
            if item.product.stock < quantity:
                raise ValueError("Not enough stock available.")
            
            item.quantity = quantity
            db.session.commit()
        
        return item
    
    @staticmethod
    def remove_from_cart(email, item_id):
        """
        Remove specific item from user's cart
        Returns: None
        """
        user = User.query.filter_by(email=email).first()
        if not user:
            return
        
        item = CartItem.query.filter_by(
            id=item_id, 
            user_id=user.id
        ).first()
        
        if item:
            db.session.delete(item)
            db.session.commit()