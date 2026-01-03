from datetime import datetime
from extensions import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from models.category import Category


# Association table for many to many relationship
offer_categories=db.Table(
  "offer_categories",
  db.Column("offer_id",db.ForeignKey("offer.id"),primary_key=True),
  db.Column("category_id",db.ForeignKey("category.id"),primary_key=True)
)

class Offer(db.Model):
  __tablename__="offer"
  id:Mapped[int]=mapped_column(primary_key=True)
  name:Mapped[str]=mapped_column(db.String(100))
  discount_percentage:Mapped[float]=mapped_column(nullable=False)
  start_date:Mapped[datetime]=mapped_column(nullable=False)
  end_date:Mapped[datetime]=mapped_column(nullable=False)

  # many to many relationship
  #it contains secondary as attribute to use that table as bridge between Offer and Category
  categories:Mapped[List["Category"]]=relationship(secondary="offer_categories", back_populates="offers")