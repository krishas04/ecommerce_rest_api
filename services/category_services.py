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
    
    @staticmethod
    def get_by_id(id):
        """Get single category by ID"""
        return Category.query.get(id)

    @staticmethod
    def update(id, data):
        """Update category fields"""
        category = Category.query.get(id)
        if category:
            if hasattr(data, 'name') and data.name:
                category.name = data.name
            db.session.commit()
        return category

    @staticmethod
    def delete(id):
        """Delete category by ID"""
        category = Category.query.get(id)
        if category:
            db.session.delete(category)
            db.session.commit()