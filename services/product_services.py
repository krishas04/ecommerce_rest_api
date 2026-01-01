from models.product import Product
from extensions import db

class ProductService:

    @staticmethod
    def add_product(product_id, name, price, stock):
        if Product.query.filter_by(id=product_id).first():
            raise ValueError("Product ID already exists.")
        
        product=Product(id=product_id, name=name, price=price, stock=stock)
        db.session.add(product)
        db.session.commit()
        return {"message": "New product added"
                }

    @staticmethod
    def lists_products():
       products=Product.query.all()
       return [{"id":p.id, "name":p.name, "price":p.price, "stock":p.stock}for p in products]