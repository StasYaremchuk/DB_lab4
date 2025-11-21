from flask import jsonify, request
from my_project.auth.service import brand_products_service


def get_all_links():
    links = brand_products_service.get_all_links()
    return jsonify(links), 200


def get_products_for_brand(brand_id: int):
    products = brand_products_service.get_products_for_brand(brand_id)
    return jsonify(products), 200


def get_brands_for_product(product_id: int):
    brands = brand_products_service.get_brands_for_product(product_id)
    return jsonify(brands), 200


def create_link():
    data = request.get_json() or {}
    if "brand_id" not in data or "product_id" not in data:
        return jsonify({"message": "brand_id and product_id are required"}), 400

    link = brand_products_service.create_link(data)
    return jsonify(link), 201


def delete_link(brand_id: int, product_id: int):
    ok = brand_products_service.delete_link(brand_id, product_id)
    if not ok:
        return jsonify({"message": "Link not found"}), 404
    return jsonify({"message": "Link deleted"}), 200