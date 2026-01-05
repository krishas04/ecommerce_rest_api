from models.product import Product
from extensions import db
from services.gallery_services import GalleryService

class ProductService:

    @staticmethod
    def add_product(product_id, name, price, stock, category_id,images):
        try:

            if Product.query.filter_by(id=product_id).first():
                raise ValueError("Product ID already exists.")
            
            #create product instance
            product=Product(id=product_id, name=name, price=price, stock=stock, category_id=category_id)

            db.session.add(product)

            # handle image uploads
            if images:
                index=0
                for file_obj in images:
                    if index==0:
                        is_primary=True
                    else:
                        is_primary=False

                    new_image=GalleryService.upload_image(file_obj, product_id,is_primary)
                
                    db.session.add(new_image)

            db.session.commit()
            return {"message": "New product added"}
        except Exception as e:
            db.session.rollback()
            raise

    @staticmethod
    def list_products():
       return Product.query.all()
    
    @staticmethod
    def get_product(product_id):
        return Product.query.get(product_id)
    
    @staticmethod
    def get_by_id(product_id):
        return Product.query.get(product_id)
    
    @staticmethod
    def update(product_id, data):
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
    
    #Delete product by ID, and Returns None
    @staticmethod
    def delete(product_id):
        product = Product.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()