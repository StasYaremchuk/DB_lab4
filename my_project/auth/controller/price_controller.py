from flask import jsonify, request
from my_project.auth.service import price_service


def get_all():
    prices = price_service.get_all_prices()
    return jsonify([p.to_dict() for p in prices]), 200


def get_one(price_id: int):
    price = price_service.get_price(price_id)
    if price is None:
        return jsonify({"message": "Price not found"}), 404
    return jsonify(price.to_dict()), 200


def create():
    data = request.get_json() or {}
    required = ("product_id", "store_id")
    if not all(k in data for k in required):
        return jsonify({"message": "product_id and store_id are required"}), 400

    price = price_service.create_price(data)
    return jsonify(price.to_dict()), 201


def update(price_id: int):
    data = request.get_json() or {}
    price = price_service.update_price(price_id, data)
    if price is None:
        return jsonify({"message": "Price not found"}), 404
    return jsonify(price.to_dict()), 200


def delete(price_id: int):
    ok = price_service.delete_price(price_id)
    if not ok:
        return jsonify({"message": "Price not found"}), 404
    return jsonify({"message": "Price deleted"}), 200