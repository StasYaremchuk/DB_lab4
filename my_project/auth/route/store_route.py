from flask import Blueprint
from my_project.auth.controller import store_controller

store_bp = Blueprint("stores", __name__)

store_bp.add_url_rule("/", view_func=store_controller.get_all, methods=["GET"])
store_bp.add_url_rule("/<int:store_id>", view_func=store_controller.get_one, methods=["GET"])
store_bp.add_url_rule("/", view_func=store_controller.create, methods=["POST"])
store_bp.add_url_rule("/<int:store_id>", view_func=store_controller.update, methods=["PUT"])
store_bp.add_url_rule("/<int:store_id>", view_func=store_controller.delete, methods=["DELETE"])