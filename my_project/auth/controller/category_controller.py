from flask import jsonify, request
from my_project.auth.service import category_service


def get_all():
    categories = category_service.get_all_categories()
    return jsonify([c.to_dict() for c in categories]), 200


def get_one(category_id: int):
    category = category_service.get_category(category_id)
    if category is None:
        return jsonify({"message": "Category not found"}), 404
    return jsonify(category.to_dict()), 200


def create():
    data = request.get_json() or {}
    if "category_name" not in data:
        return jsonify({"message": "category_name is required"}), 400
    category = category_service.create_category(data)
    return jsonify(category.to_dict()), 201


def update(category_id: int):
    data = request.get_json() or {}
    category = category_service.update_category(category_id, data)
    if category is None:
        return jsonify({"message": "Category not found"}), 404
    return jsonify(category.to_dict()), 200


def delete(category_id: int):
    ok = category_service.delete_category(category_id)
    if not ok:
        return jsonify({"message": "Category not found"}), 404
    return jsonify({"message": "Category deleted"}), 200