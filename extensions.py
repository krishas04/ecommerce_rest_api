from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import DeclarativeBase
from flask_marshmallow import Marshmallow

class Base(DeclarativeBase):
    pass

# Pass the custom Base to SQLAlchemy
db = SQLAlchemy(model_class=Base)
migrate = Migrate()
ma = Marshmallow()