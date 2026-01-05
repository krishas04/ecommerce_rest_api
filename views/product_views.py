import traceback
from flask.views import MethodView
from flask import jsonify, request
from datetime import datetime, timezone
from marshmallow import ValidationError
from services.product_services import ProductService
from schemas.product_schema import ProductSchema, product_schema, products_schema
from middleware.auth_middleware import token_required
from views.base_api import BaseAPI


class ProductListAPI(BaseAPI):
    # Handle product collection endpoint
    def get(self):
        # GET /products - List all products
        try:
            # Get all products from service
            products = ProductService.list_products()
            
            # Serialize using schema
            return jsonify(products_schema.dump(products)), 200
            
        except Exception as e:
            return self.error_response("Invalid server error", 500)
    
    @token_required
    def post(self):
        # POST /products - Create new product (requires auth)
        try:
            images=None

            # for multipart request
            if request.content_type.startswith("multipart/form-data"):
                data=product_schema.load(request.form)
                images=request.files.getlist("images")

                result=ProductService.add_product(
                    data.id,
                    data.name,
                    data.price,
                    data.stock,
                    data.category_id,
                    images=images
                )
                return self.success_response(result,201)
            # for json request
            elif request.is_json:
                # Validate and load data
                data = product_schema.load(request.get_json())
                
                # Create product in database
                result = ProductService.add_product(
                    data.id,
                    data.name,
                    data.price,
                    data.stock,
                    data.category_id,
                    images=None
                )
                
                # Return 201 Created
                return self.success_response(result,201)
            
            else:
                return self.error_response("Response must be json or multipart data",400)
            
        except ValidationError as e:
            return self.error_response(str(e),400)
        except Exception as e:
            tb = traceback.format_exc()  # get full traceback
            return self.error_response(f"Internal Server Error:\n{tb}", 500)

class ProductDetailAPI(BaseAPI):
    # Handle single product endpoint 
    
    def get(self, product_id):
        # GET /products/<id> - Get single product
        try:
            # Get product by ID
            product = ProductService.get_product(product_id)
            if not product:
                return self.error_response("Product not found", 404)
            
            return jsonify(product_schema.dump(product)), 200
            
        except Exception as e:
            return self.error_response("Internal server error", 500)
    
    @token_required
    def patch(self, product_id):
        # PATCH /products/<id> - Update product
        try:
            # Check if product exists
            product = ProductService.get_product(product_id)
            if not product:
                return self.error_response("Product not found", 404)
            
            # Validate and load data
            data = product_schema.load(request.get_json(), partial=True)
            
            # Update in database
            updated = ProductService.update(product_id, data)
            
            return jsonify(product_schema.dump(updated)), 200
            
        except ValidationError as e:
            return self.error_response(str(e))
        except Exception as e:
            return self.error_response("Internal server error",500)
    
    @token_required
    def delete(self, product_id):
        # DELETE /products/<id> - Delete product
        try:
            product = ProductService.get_product(product_id)
            if not product:
                return self.error_response("Product not found", 404)
            
            # Delete from database
            ProductService.delete(product_id)
            
            # Return 204 No Content
            return "", 204
            
        except Exception as e:
            return self.error_response("Internal server error",500)

