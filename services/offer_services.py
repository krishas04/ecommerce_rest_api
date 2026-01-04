from models.offer import Offer
from models.category import Category
from extensions import db
from utils.time import normalize_to_utc

class OfferService:
    @staticmethod
    def create_offer(name, discount, start, end, category_ids):
        # 1. Create the offer object
        new_offer = Offer(
            name=name,
            discount_percentage=discount,
            start_date=normalize_to_utc(start),
            end_date=normalize_to_utc(end)
            #dont pass category_ids here
        )

        # 2. Link categories (Many-to-Many)
        categories = Category.query.filter(Category.id.in_(category_ids)).all()
        if not categories:
            raise ValueError("At least one valid category ID is required.")
        
        new_offer.categories = categories # SQLAlchemy handles the association table
        
        db.session.add(new_offer)
        db.session.commit()
        return new_offer
    
    @staticmethod
    def get_all_offers():
        return Offer.query.all()
    
    @staticmethod
    def get_by_id(id):
        """
        Get single offer by ID
        Returns: Offer object or None
        """
        return Offer.query.get(id)
    
    @staticmethod
    def update(id, data):
        """
        Update offer fields
        data: Offer object or dict with updated fields
        Returns: Updated offer object
        """
        offer = Offer.query.get(id)
        if offer:
            # Update name if provided
            if hasattr(data, 'name') and data.name:
                offer.name = data.name
            
            # Update discount percentage if provided
            if hasattr(data, 'discount_percentage'):
                offer.discount_percentage = data.discount_percentage
            
            # Update start date if provided
            if hasattr(data, 'start_date') and data.start_date:
                offer.start_date = normalize_to_utc(data.start_date)
            
            # Update end date if provided
            if hasattr(data, 'end_date') and data.end_date:
                offer.end_date = normalize_to_utc(data.end_date)
            
            # Commit changes
            db.session.commit()
        
        return offer
    
    @staticmethod
    def delete(id):
        """
        Delete offer by ID
        Returns: None
        """
        offer = Offer.query.get(id)
        if offer:
            db.session.delete(offer)
            db.session.commit()