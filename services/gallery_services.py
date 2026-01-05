import os
from pathlib import Path
import secrets
from flask import current_app
from werkzeug.utils import secure_filename
from models.gallery import ProductImage
from extensions import db

class GalleryService:
    ALLOWED_EXTENSIONS={".png", ".jpg", ".jpeg"}
    ALLOWED_MIMETYPES={"image.png", "image/jpeg"}

    @staticmethod
    def upload_image(file_obj, product_id, is_primary=False):
        file_path=Path(file_obj.filename)
        extension=file_path.suffix.lower()

        if extension not in GalleryService.ALLOWED_EXTENSIONS:
            raise ValueError(f"Extension {extension} not allowed")
        
        if file_obj.mimetype not in GalleryService.ALLOWED_MIMETYPES:
            raise ValueError(f"Mimetype {file_obj.mimetype} not allowed")
        
        unique_prefix=secrets.token_hex(4)
        clean_name = os.path.splitext(secure_filename(file_obj.filename))[0]
        unique_filename=f"{unique_prefix}_{clean_name}{extension}"
        
        upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], unique_filename)
        file_obj.save(upload_path)
        
        # 4. Save metadata to Database
        new_image = ProductImage(
            filename=unique_filename,
            original_name=clean_name,
            product_id=product_id,
            is_primary=is_primary
        )
        db.session.add(new_image)
        db.session.commit()
        
        return new_image

    @staticmethod
    def get_product_images(product_id):
        return ProductImage.query.filter_by(product_id=product_id).all()