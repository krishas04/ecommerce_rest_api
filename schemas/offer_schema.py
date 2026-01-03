from extensions import ma, db
from models.offer import Offer
from marshmallow import fields

class OfferSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Offer
        load_instance = True
        sqla_session = db.session
        include_fk = True

    # Ensure dates are handled as ISO strings
    start_date = fields.DateTime(required=True)
    end_date = fields.DateTime(required=True)
     # load_only=True prevents errors when dumping the object later
    category_ids = fields.List(fields.Int(), required=True, load_only=True)

offer_schema = OfferSchema()
offers_schema = OfferSchema(many=True)