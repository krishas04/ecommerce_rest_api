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