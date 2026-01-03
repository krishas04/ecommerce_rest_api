from extensions import ma
from models.cart import CartItem
from marshmallow import fields

class CartItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CartItem
        load_instance = True
        include_fk = True # Includes user_id and product_id

    product = fields.Nested("ProductSchema")
    subtotal = fields.Method("get_subtotal")

    def get_subtotal(self, obj):
        return round(obj.quantity * obj.product.get_current_price(),2)

cart_item_schema = CartItemSchema()
cart_items_schema = CartItemSchema(many=True)