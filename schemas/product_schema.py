from extensions import ma,db
from models.product import Product
from marshmallow import fields

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True

    # Custom field validation
    price = fields.Float(required=True, validate=lambda x: x > 0)
    stock = fields.Int(required=True, validate=lambda x: x >= 0)

product_schema = ProductSchema(session=db.session)
products_schema = ProductSchema(many=True,session=db.session)