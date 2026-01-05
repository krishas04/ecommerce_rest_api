from flask import request, jsonify
from flask.views import MethodView
from services.gallery_services import GalleryService
from schemas.gallery_schema import gallery_schema, gallery_list_schema

class GalleryAPI(MethodView):
    
    def get(self,product_id):
        images = GalleryService.get_product_images(product_id)
        return jsonify(gallery_list_schema.dump(images)), 200

    def post(self,product_id):
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        
        image_file = request.files['file']
        
        if image_file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        # Use the service to handle the upload
        try:
            new_image = GalleryService.upload_image(image_file, product_id=product_id,is_primary=False)
            return jsonify(gallery_schema.dump(new_image)), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500