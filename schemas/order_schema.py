from extensions import ma
from models.order import Order, OrderItem
from marshmallow import fields

class OrderItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OrderItem
        load_instance = True
    
   
    id = fields.Int(dump_only=True)

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        load_instance = True
        include_fk = True

    # Nested relationship: Show all items belonging to this order
    items = fields.List(fields.Nested(OrderItemSchema))
    
    # Format the date nicely for the frontend
    created_at = fields.DateTime(format="%Y-%m-%d %H:%M:%S")


order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)