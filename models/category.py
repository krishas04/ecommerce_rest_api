from extensions import db
from sqlalchemy.orm import Mapped, mapped_column,relationship
from typing import TYPE_CHECKING, List
if TYPE_CHECKING:
    from models.offer import Offer
    from models.product import Product

class Category(db.Model):
  id:Mapped[int]=mapped_column(primary_key=True)
  name:Mapped[str]=mapped_column(db.String(100),unique=True)
  products:Mapped[List["Product"]]=relationship(back_populates="category")
  offers:Mapped[List["Offer"]]=relationship(secondary="offer_categories",back_populates="categories")