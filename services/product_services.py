from models.product import Product
from extensions import db

class ProductService:

    @staticmethod
    def add_product(product_id, name, price, stock, category_id):
        if Product.query.filter_by(id=product_id).first():
            raise ValueError("Product ID already exists.")
        
        product=Product(id=product_id, name=name, price=price, stock=stock, category_id=category_id)
        db.session.add(product)
        db.session.commit()
        return {"message": "New product added"
                }

    @staticmethod
    def lists_products():
       return Product.query.all()
    
    @staticmethod
    def get_product(product_id):
        return Product.query.get(product_id)
    
    @staticmethod
    def get_by_id(product_id):
        """
        Get single product by ID
        Returns: Product object or None
        """
        return Product.query.get(product_id)
    
    @staticmethod
    def update(product_id, data):
        """
        Update product fields
        data: Product object or dict with updated fields
        Returns: Updated product object
        """
        product = Product.query.get(product_id)
        if product:
            # Update name if provided
            if hasattr(data, 'name') and data.name:
                product.name = data.name
            
            # Update price if provided
            if hasattr(data, 'price') and data.price is not None:
                product.price = data.price
            
            # Update stock if provided
            if hasattr(data, 'stock') and data.stock is not None:
                product.stock = data.stock
            
            # Update category_id if provided
            if hasattr(data, 'category_id') and data.category_id is not None:
                product.category_id = data.category_id
            
            # Commit changes
            db.session.commit()
        
        return product
    
    @staticmethod
    def delete(product_id):
        """
        Delete product by ID
        Returns: None
        """
        product = Product.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()