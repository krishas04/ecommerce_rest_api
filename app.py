from flask import Flask
from config import Config
from extensions import db, migrate, ma
import models
from api.auth_api import auth_bp
from api.product_api import product_bp
from api.cart_api import cart_bp
from api.order_api import order_bp
from api.offer_api import offer_bp
from api.category_api import category_bp
from api.gallery_api import gallery_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)  # Connects SQLAlchemy to this app instance.
    migrate.init_app(app, db) # Connects Flask-Migrate to handle schema migrations.
    ma.init_app(app)
    

    # temporarily activates the app so Flask knows which application, config, and database to use when running code outside a request.
    with app.app_context(): #
      db.create_all() # Automatically creates the .db file and tables

    # Register Blueprints with URL prefixes
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(product_bp, url_prefix='/products')
    app.register_blueprint(cart_bp, url_prefix='/cart')
    app.register_blueprint(order_bp, url_prefix='/orders')
    app.register_blueprint(category_bp, url_prefix='/categories')
    app.register_blueprint(offer_bp, url_prefix='/offers')
    app.register_blueprint(gallery_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)