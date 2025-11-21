from flask import Blueprint
from my_project.auth.controller import category_controller

category_bp = Blueprint("categories", __name__)

category_bp.add_url_rule("/", view_func=category_controller.get_all, methods=["GET"])
category_bp.add_url_rule("/<int:category_id>", view_func=category_controller.get_one, methods=["GET"])
category_bp.add_url_rule("/", view_func=category_controller.create, methods=["POST"])
category_bp.add_url_rule("/<int:category_id>", view_func=category_controller.update, methods=["PUT"])
category_bp.add_url_rule("/<int:category_id>", view_func=category_controller.delete, methods=["DELETE"])