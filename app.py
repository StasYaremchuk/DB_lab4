from flask import Flask
import os
import yaml

from my_project.auth.route.country_route import country_bp
from my_project.auth.route.address_route import address_bp
from my_project.auth.route.brand_route import brand_bp
from my_project.auth.route.category_route import category_bp
from my_project.auth.route.product_route import product_bp
from my_project.auth.route.store_route import store_bp
from my_project.auth.route.price_route import price_bp
from my_project.auth.route.contact_route import contact_bp
from my_project.auth.route.website_route import website_bp
from my_project.auth.route.brand_products_route import brand_products_bp


def create_app() -> Flask:
    app = Flask(__name__)

    config_path = os.path.join(os.path.dirname(__file__), "config", "app.yml")
    with open(config_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    app.config["APP_CONFIG"] = cfg

    app.register_blueprint(country_bp, url_prefix="/api/countries")
    app.register_blueprint(address_bp, url_prefix="/api/addresses")
    app.register_blueprint(brand_bp, url_prefix="/api/brands")
    app.register_blueprint(category_bp, url_prefix="/api/categories")
    app.register_blueprint(product_bp, url_prefix="/api/products")
    app.register_blueprint(store_bp, url_prefix="/api/stores")
    app.register_blueprint(price_bp, url_prefix="/api/prices")
    app.register_blueprint(contact_bp, url_prefix="/api/contacts")
    app.register_blueprint(website_bp, url_prefix="/api/websites")
    app.register_blueprint(brand_products_bp, url_prefix="/api/brand-products")

    return app


app = create_app()

if __name__ == "__main__":
    flask_cfg = app.config["APP_CONFIG"]["flask"]
    app.run(
        host=flask_cfg.get("host", "127.0.0.1"),
        port=flask_cfg.get("port", 5000),
        debug=flask_cfg.get("debug", True),
    )