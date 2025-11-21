from flask import Blueprint
from my_project.auth.controller import price_controller

price_bp = Blueprint("prices", __name__)

price_bp.add_url_rule("/", view_func=price_controller.get_all, methods=["GET"])
price_bp.add_url_rule("/<int:price_id>", view_func=price_controller.get_one, methods=["GET"])
price_bp.add_url_rule("/", view_func=price_controller.create, methods=["POST"])
price_bp.add_url_rule("/<int:price_id>", view_func=price_controller.update, methods=["PUT"])
price_bp.add_url_rule("/<int:price_id>", view_func=price_controller.delete, methods=["DELETE"])