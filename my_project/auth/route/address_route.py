from flask import Blueprint
from my_project.auth.controller import address_controller

address_bp = Blueprint("addresses", __name__)

address_bp.add_url_rule("/", view_func=address_controller.get_all, methods=["GET"])
address_bp.add_url_rule("/<int:address_id>", view_func=address_controller.get_one, methods=["GET"])
address_bp.add_url_rule("/", view_func=address_controller.create, methods=["POST"])
address_bp.add_url_rule("/<int:address_id>", view_func=address_controller.update, methods=["PUT"])
address_bp.add_url_rule("/<int:address_id>", view_func=address_controller.delete, methods=["DELETE"])