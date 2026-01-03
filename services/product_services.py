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