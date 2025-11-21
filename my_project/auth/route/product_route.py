from flask import Blueprint
from my_project.auth.controller import product_controller

product_bp = Blueprint("products", __name__)

product_bp.add_url_rule("/", view_func=product_controller.get_all, methods=["GET"])
product_bp.add_url_rule("/<int:product_id>", view_func=product_controller.get_one, methods=["GET"])
product_bp.add_url_rule("/", view_func=product_controller.create, methods=["POST"])
product_bp.add_url_rule("/<int:product_id>", view_func=product_controller.update, methods=["PUT"])
product_bp.add_url_rule("/<int:product_id>", view_func=product_controller.delete, methods=["DELETE"])

product_bp.add_url_rule(
    "/<int:product_id>/brands",
    view_func=product_controller.get_brands,
    methods=["GET"],
)