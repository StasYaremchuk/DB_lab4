from flask import Blueprint
from my_project.auth.controller import country_controller

country_bp = Blueprint("countries", __name__)

country_bp.add_url_rule("/", view_func=country_controller.get_all, methods=["GET"])
country_bp.add_url_rule("/<int:country_id>", view_func=country_controller.get_one, methods=["GET"])
country_bp.add_url_rule("/", view_func=country_controller.create, methods=["POST"])
country_bp.add_url_rule("/<int:country_id>", view_func=country_controller.update, methods=["PUT"])
country_bp.add_url_rule("/<int:country_id>", view_func=country_controller.delete, methods=["DELETE"])

country_bp.add_url_rule(
    "/<int:country_id>/addresses",
    view_func=country_controller.get_addresses,
    methods=["GET"],
)

country_bp.add_url_rule(
    "/addresses",
    view_func=country_controller.get_all_with_addresses,
    methods=["GET"],
)