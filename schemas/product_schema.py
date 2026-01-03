from extensions import ma,db
from models.product import Product
from marshmallow import fields

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True
        include_fk=True

    # Regular fields with Custom field validation
    price = fields.Float(required=True, validate=lambda x: x > 0)
    stock = fields.Int(required=True, validate=lambda x: x >= 0)
    # Method fields
    discounted_price = fields.Method("get_discounted_price")
    active_offer_name = fields.Method("get_offer_name")

    def get_discounted_price(self, obj):
        return obj.get_current_price()
    
    def get_offer_name(self, obj):
        offer = obj.get_active_offer()
        return offer.name if offer else None
            

product_schema = ProductSchema(session=db.session)
products_schema = ProductSchema(many=True,session=db.session)