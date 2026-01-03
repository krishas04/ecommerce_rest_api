from extensions import ma, db
from models.category import Category

class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        load_instance = True
        sqla_session = db.session

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)