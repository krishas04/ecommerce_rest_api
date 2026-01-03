from flask import Blueprint, request, jsonify
from services.category_services import CategoryService
from schemas.category_schema import category_schema, categories_schema
from middleware.auth_middleware import token_required
from marshmallow import ValidationError

category_bp = Blueprint('categories', __name__)

@category_bp.route('', methods=['GET'])
def list_categories():
    """
    GET /categories
    Returns a list of all available categories.
    """
    categories = CategoryService.get_all()
    # Serialize the list of category objects into JSON
    return jsonify(categories_schema.dump(categories)), 200

@category_bp.route('', methods=['POST'])
@token_required
def add_category():
    """
    POST /categories
    Creates a new category. Requires a valid JWT token.
    Body: { "name": "Electronics" }
    """
    try:
        # 1. Validate the incoming JSON data using Marshmallow
        # load() ensures the 'name' is provided and valid
        data = category_schema.load(request.get_json())
        
        # 2. Call the service to save to the database
        # 'data' is a Category model instance because of load_instance=True
        new_category = CategoryService.add_category(data.name)
        
        # 3. Return the created category as JSON
        return jsonify(category_schema.dump(new_category)), 201

    except ValidationError as e:
        # Returns automatic error messages (e.g., if 'name' is missing)
        return jsonify(e.messages), 400
    except Exception as e:
        # Handle database errors (like unique constraint if name already exists)
        return jsonify({"error": str(e)}), 400