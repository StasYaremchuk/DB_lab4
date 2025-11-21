from flask import Blueprint
from my_project.auth.controller import website_controller

website_bp = Blueprint("websites", __name__)

website_bp.add_url_rule("/", view_func=website_controller.get_all, methods=["GET"])
website_bp.add_url_rule("/<int:website_id>", view_func=website_controller.get_one, methods=["GET"])
website_bp.add_url_rule("/", view_func=website_controller.create, methods=["POST"])
website_bp.add_url_rule("/<int:website_id>", view_func=website_controller.update, methods=["PUT"])
website_bp.add_url_rule("/<int:website_id>", view_func=website_controller.delete, methods=["DELETE"])