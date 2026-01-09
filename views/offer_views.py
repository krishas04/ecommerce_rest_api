from flask.views import MethodView
from flask import jsonify, request
from marshmallow import ValidationError
from services.offer_services import OfferService
from schemas.offer_schema import offer_schema, offers_schema
from middleware.auth_middleware import token_required
from views.base_api import BaseAPI


class OfferListAPI(BaseAPI):
    
    def get(self):
        try:
            # Get all offers from service
            offers = OfferService.get_all_offers()
            
            return jsonify(offers_schema.dump(offers)), 200
            
        except Exception as e:
            return self.error_response(str(e), 500)
    
    @token_required
    def post(self):
        try:
            data = offer_schema.load(request.get_json())
            
            category_ids = request.get_json().get('category_ids')
            
            offer = OfferService.create_offer(
                name=data.name,
                discount=data.discount_percentage,
                start=data.start_date,
                end=data.end_date,
                category_ids=category_ids
            )
            
            return jsonify(offer_schema.dump(offer)), 201
            
        except ValidationError as e:
            return jsonify(e.messages), 400
        except Exception as e:
            return self.error_response(str(e))


class OfferDetailAPI(BaseAPI):
    
    def get(self, id):
        try:
            # Get offer by ID
            offer = OfferService.get_by_id(id)
            if not offer:
                return self.error_response("Offer not found", 404)
            
            return jsonify(offer_schema.dump(offer)), 200
            
        except Exception as e:
            return self.error_response(str(e), 500)
    
    @token_required
    def patch(self, id):
        try:
            # Check if offer exists
            offer = OfferService.get_by_id(id)
            if not offer:
                return self.error_response("Offer not found", 404)
            
            # Validate and load data
            data = offer_schema.load(request.get_json(), partial=True)
            
            # Update in database
            updated = OfferService.update(id, data)
            
            return jsonify(offer_schema.dump(updated)), 200
            
        except ValidationError as e:
            return jsonify(e.messages), 400
        except Exception as e:
            return self.error_response(str(e))
    
    @token_required
    def delete(self, id):
        try:
            offer = OfferService.get_by_id(id)
            if not offer:
                return self.error_response("Offer not found", 404)
            
            # Delete from database
            OfferService.delete(id)
            
            return "", 204
            
        except Exception as e:
            return self.error_response(str(e))