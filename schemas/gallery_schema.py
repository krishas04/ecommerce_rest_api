from extensions import ma
from models.gallery import ProductImage
from marshmallow import fields
from flask import url_for

class GallerySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductImage
        load_instance = True

    # This creates a clickable URL
    image_url = fields.Method("get_image_url")

    def get_image_url(self, obj):
        # Generates: http://localhost:5000/static/uploads/gallery/unique_name.jpg
        return url_for('static', filename=f'uploads/gallery/{obj.filename}', _external=True)

gallery_schema = GallerySchema()
gallery_list_schema = GallerySchema(many=True)