from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from extensions import db

if TYPE_CHECKING:
    from models.product import Product

class CartItem(db.Model):
    __tablename__ = "cart_item"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    product_id: Mapped[str] = mapped_column(ForeignKey('product.id'), nullable=False)
    quantity: Mapped[int] = mapped_column(default=1)

    product: Mapped["Product"] = relationship()