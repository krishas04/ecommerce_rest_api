from flask import Flask
from config import Config
from extensions import db, migrate
from api.auth_api import auth_bp
from api.product_api import product_bp
from api.cart_api import cart_bp
from api.order_api import order_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)  # Connects SQLAlchemy to this app instance.
    migrate.init_app(app, db) # Connects Flask-Migrate to handle schema migrations.

    # temporarily activates the app so Flask knows which application, config, and database to use when running code outside a request.
    with app.app_context(): #
      db.create_all() # Automatically creates the .db file and tables

    # Register Blueprints with URL prefixes
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(product_bp, url_prefix='/products')
    app.register_blueprint(cart_bp, url_prefix='/cart')
    app.register_blueprint(order_bp, url_prefix='/orders')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)