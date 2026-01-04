from flask import Blueprint, request, jsonify
from services.offer_services import OfferService
from schemas.offer_schema import offer_schema, offers_schema
from middleware.auth_middleware import token_required

offer_bp = Blueprint('offers', __name__)

@offer_bp.route('', methods=['POST'])
@token_required
def add_offer():
    try:
        data = offer_schema.load(request.get_json())
         # We extract category_ids from raw json because it's a load_only field
        category_ids=request.get_json().get('category_ids') 
        # We manually pass data to service to handle M2M linking
        offer = OfferService.create_offer(
            name=data.name,
            discount=data.discount_percentage,
            start=data.start_date,
            end=data.end_date,
            category_ids=category_ids
        )
        return jsonify(offer_schema.dump(offer)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@offer_bp.route('', methods=['GET'])
def list_offers():
    all_offers=OfferService.get_all_offers()
    return jsonify(offers_schema.dump(all_offers))