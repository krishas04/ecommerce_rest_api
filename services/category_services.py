from models.category import Category
from extensions import db

class CategoryService:
    @staticmethod
    def add_category(name):
        category = Category(name=name)
        db.session.add(category)
        db.session.commit()
        return category

    @staticmethod
    def get_all():
        return Category.query.all()