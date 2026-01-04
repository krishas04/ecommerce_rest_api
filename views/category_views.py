from flask.views import MethodView
from flask import jsonify, request
from services.category_services import CategoryService
from schemas.category_schema import category_schema, categories_schema
from middleware.auth_middleware import token_required
from views.base_api import BaseAPI
from marshmallow import ValidationError

# Class 1: Handle /categories (collection)
class CategoryListAPI(BaseAPI):
    """
    Maps to:
    - GET /categories
    - POST /categories
    """
    
    def get(self):
        """GET /categories - List all categories"""
        try:
            categories = CategoryService.get_all()
            return jsonify(categories_schema.dump(categories)), 200
        except Exception as e:
            return self.error_response(str(e), 500)
    
    @token_required  # Decorator works on class methods!
    def post(self):
        """POST /categories - Create new category"""
        try:
            data = category_schema.load(request.get_json())
            new_category = CategoryService.add_category(data.name)
            return jsonify(category_schema.dump(new_category)), 201
        except ValidationError as e:
            return jsonify(e.messages), 400
        except Exception as e:
            return self.error_response(str(e))


# Class 2: Handle /categories/<id> (single item)
class CategoryDetailAPI(BaseAPI):
    """
    Maps to:
    - GET /categories/<id>
    - PATCH /categories/<id>
    - DELETE /categories/<id>
    """
    
    def get(self, id):
        """GET /categories/<id> - Get single category"""
        try:
            category = CategoryService.get_by_id(id)
            if not category:
                return self.error_response("Category not found", 404)
            return jsonify(category_schema.dump(category)), 200
        except Exception as e:
            return self.error_response(str(e), 500)
    
    @token_required
    def patch(self, id):
        """PATCH /categories/<id> - Update category"""
        try:
            category = CategoryService.get_by_id(id)
            if not category:
                return self.error_response("Category not found", 404)
            
            data = category_schema.load(request.get_json(), partial=True)
            updated = CategoryService.update(id, data)
            return jsonify(category_schema.dump(updated)), 200
        except Exception as e:
            return self.error_response(str(e))
    
    @token_required
    def delete(self, id):
        """DELETE /categories/<id> - Delete category"""
        try:
            category = CategoryService.get_by_id(id)
            if not category:
                return self.error_response("Category not found", 404)
            
            CategoryService.delete(id)
            return "", 204  # No content response
        except Exception as e:
            return self.error_response(str(e))