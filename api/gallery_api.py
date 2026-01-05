from flask import Blueprint
from views.gallery_views import GalleryAPI

gallery_bp = Blueprint('gallery', __name__)
gallery_view = GalleryAPI.as_view('gallery_api')
gallery_bp.add_url_rule('/gallery', view_func=gallery_view, methods=['GET', 'POST'])
