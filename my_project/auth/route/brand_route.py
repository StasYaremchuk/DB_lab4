from flask import Blueprint
from my_project.auth.controller import brand_controller

brand_bp = Blueprint("brands", __name__)

brand_bp.add_url_rule("/", view_func=brand_controller.get_all, methods=["GET"])
brand_bp.add_url_rule("/<int:brand_id>", view_func=brand_controller.get_one, methods=["GET"])
brand_bp.add_url_rule("/", view_func=brand_controller.create, methods=["POST"])
brand_bp.add_url_rule("/<int:brand_id>", view_func=brand_controller.update, methods=["PUT"])
brand_bp.add_url_rule("/<int:brand_id>", view_func=brand_controller.delete, methods=["DELETE"])

brand_bp.add_url_rule(
    "/<int:brand_id>/products",
    view_func=brand_controller.get_products,
    methods=["GET"],
)