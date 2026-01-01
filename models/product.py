from sqlalchemy.orm import Mapped, mapped_column
from extensions import db

class Product(db.Model):
    id: Mapped[str] = mapped_column(db.String(50), primary_key=True)
    name: Mapped[str] = mapped_column(db.String(100), nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    stock: Mapped[int] = mapped_column(default=0)