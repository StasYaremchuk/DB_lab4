from flask import Blueprint
from my_project.auth.controller import brand_products_controller

brand_products_bp = Blueprint("brand_products", __name__)

brand_products_bp.add_url_rule(
    "/", view_func=brand_products_controller.get_all_links, methods=["GET"]
)
brand_products_bp.add_url_rule(
    "/", view_func=brand_products_controller.create_link, methods=["POST"]
)

brand_products_bp.add_url_rule(
    "/brands/<int:brand_id>/products",
    view_func=brand_products_controller.get_products_for_brand,
    methods=["GET"],
)

brand_products_bp.add_url_rule(
    "/products/<int:product_id>/brands",
    view_func=brand_products_controller.get_brands_for_product,
    methods=["GET"],
)

brand_products_bp.add_url_rule(
    "/<int:brand_id>/<int:product_id>",
    view_func=brand_products_controller.delete_link,
    methods=["DELETE"],
)