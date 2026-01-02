from extensions import ma
from models.cart import CartItem
from marshmallow import fields

class CartItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CartItem
        load_instance = True
        include_fk = True # Includes user_id and product_id

    product = fields.Nested("ProductSchema", only=("name", "price"))
    subtotal = fields.Method("get_subtotal")

    def get_subtotal(self, obj):
        return obj.quantity * obj.product.price

cart_item_schema = CartItemSchema()
cart_items_schema = CartItemSchema(many=True)