from extensions import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

class ProductImage(db.Model):
    __tablename__="productimage"
    id: Mapped[int] = mapped_column(primary_key=True)
    filename: Mapped[str] = mapped_column(db.String(255), nullable=False)
    original_name: Mapped[str] = mapped_column(db.String(255))
    # one product has many images
    product_id:Mapped[str]= mapped_column(ForeignKey('product.id'), nullable=False)
    product=relationship("Product",back_populates="images")

    #it decides which is the main image
    is_primary:Mapped[bool]=mapped_column(default=False)