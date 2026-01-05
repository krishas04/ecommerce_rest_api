from models.gallery import ProductImage
from sqlalchemy.orm import Mapped, mapped_column, relationship
from extensions import db
from typing import TYPE_CHECKING, List

from utils.time import normalize_to_utc, now_utc
if TYPE_CHECKING:
    from models.category import Category

class Product(db.Model):
    __tablename__="product"
    id: Mapped[str] = mapped_column(db.String(50), primary_key=True)
    name: Mapped[str] = mapped_column(db.String(100), nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    stock: Mapped[int] = mapped_column(default=0)
    category_id:Mapped[int]=mapped_column(db.ForeignKey('category.id'), nullable=True)
    category:Mapped["Category"]=relationship(back_populates="products")

    #for image(one product has many images)
    images:Mapped[List["ProductImage"]]=relationship(back_populates="product",cascade="all, delete-orphan",lazy="selectin")

    #business logic
    def get_active_offer(self):
        # Returns the highest percentage discount offer currently active.
        if not self.category or not self.category.offers:
            return None
        
        now = now_utc()
        best_offer = None
        
        for offer in self.category.offers:
           start = normalize_to_utc(offer.start_date)
           end = normalize_to_utc(offer.end_date)
            
           if start <= now <= end:
                if not best_offer or offer.discount_percentage > best_offer.discount_percentage:
                    best_offer = offer
        return best_offer

    def get_current_price(self):
        # Returns the price after applying the best active discount.
        offer = self.get_active_offer()
        if offer:
            discount = self.price * (offer.discount_percentage / 100)
            return round(self.price - discount, 2)
        return self.price