from flask import jsonify, request
from my_project.auth.service import product_service, brand_products_service


def get_all():
    products = product_service.get_all_products()
    return jsonify([p.to_dict() for p in products]), 200


def get_one(product_id: int):
    product = product_service.get_product(product_id)
    if product is None:
        return jsonify({"message": "Product not found"}), 404
    return jsonify(product.to_dict()), 200


def create():
    data = request.get_json() or {}
    required = ("product_name", "category_id")
    if not all(k in data for k in required):
        return jsonify({"message": "product_name and category_id are required"}), 400

    product = product_service.create_product(data)
    return jsonify(product.to_dict()), 201


def update(product_id: int):
    data = request.get_json() or {}
    product = product_service.update_product(product_id, data)
    if product is None:
        return jsonify({"message": "Product not found"}), 404
    return jsonify(product.to_dict()), 200


def delete(product_id: int):
    ok = product_service.delete_product(product_id)
    if not ok:
        return jsonify({"message": "Product not found"}), 404
    return jsonify({"message": "Product deleted"}), 200


def get_brands(product_id: int):
    product = product_service.get_product(product_id)
    if product is None:
        return jsonify({"message": "Product not found"}), 404

    brands = brand_products_service.get_brands_for_product(product_id)
    return jsonify([b.to_dict() for b in brands]), 200