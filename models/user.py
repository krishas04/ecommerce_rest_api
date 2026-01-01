from typing import List, TYPE_CHECKING # Import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from extensions import db

# This block is only read by IDEs/Type Checkers, NOT by Python at runtime.
# This prevents the circular import.
if TYPE_CHECKING:
    from models.order import Order

class User(db.Model):
    __tablename__ = "user" # Explicitly naming tables is good practice
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(db.String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String(255), nullable=True)
    
    # Use the string name "Order" instead of the class Order
    orders: Mapped[List["Order"]] = relationship(back_populates="user", lazy=True)