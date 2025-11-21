from flask import Blueprint
from my_project.auth.controller import contact_controller

contact_bp = Blueprint("contacts", __name__)

contact_bp.add_url_rule("/", view_func=contact_controller.get_all, methods=["GET"])
contact_bp.add_url_rule("/<int:contact_id>", view_func=contact_controller.get_one, methods=["GET"])
contact_bp.add_url_rule("/", view_func=contact_controller.create, methods=["POST"])
contact_bp.add_url_rule("/<int:contact_id>", view_func=contact_controller.update, methods=["PUT"])
contact_bp.add_url_rule("/<int:contact_id>", view_func=contact_controller.delete, methods=["DELETE"])