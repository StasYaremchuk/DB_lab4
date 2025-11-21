from flask import jsonify, request
from my_project.auth.service import brand_service
from my_project.auth.service import brand_products_service


def get_all():
    brands = brand_service.get_all_brands()
    return jsonify([b.to_dict() for b in brands]), 200


def get_one(brand_id: int):
    brand = brand_service.get_brand(brand_id)
    if brand is None:
        return jsonify({"message": "Brand not found"}), 404
    return jsonify(brand.to_dict()), 200


def create():
    data = request.get_json() or {}
    if "brand_name" not in data:
        return jsonify({"message": "brand_name is required"}), 400
    brand = brand_service.create_brand(data)
    return jsonify(brand.to_dict()), 201


def update(brand_id: int):
    data = request.get_json() or {}
    brand = brand_service.update_brand(brand_id, data)
    if brand is None:
        return jsonify({"message": "Brand not found"}), 404
    return jsonify(brand.to_dict()), 200


def delete(brand_id: int):
    ok = brand_service.delete_brand(brand_id)
    if not ok:
        return jsonify({"message": "Brand not found"}), 404
    return jsonify({"message": "Brand deleted"}), 200


def get_products(brand_id: int):

    brand = brand_service.get_brand(brand_id)
    if brand is None:
        return jsonify({"message": "Brand not found"}), 404

    products = brand_products_service.get_products_for_brand(brand_id)
    return jsonify([p.to_dict() for p in products]), 200