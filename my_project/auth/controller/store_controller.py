from flask import jsonify, request
from my_project.auth.service import store_service


def get_all():
    stores = store_service.get_all_stores()
    return jsonify([s.to_dict() for s in stores]), 200


def get_one(store_id: int):
    store = store_service.get_store(store_id)
    if store is None:
        return jsonify({"message": "Store not found"}), 404
    return jsonify(store.to_dict()), 200


def create():
    data = request.get_json() or {}
    required = ("store_name", "brand_id", "address_id")
    if not all(k in data for k in required):
        return jsonify({"message": "store_name, brand_id, address_id are required"}), 400

    store = store_service.create_store(data)
    return jsonify(store.to_dict()), 201


def update(store_id: int):
    data = request.get_json() or {}
    store = store_service.update_store(store_id, data)
    if store is None:
        return jsonify({"message": "Store not found"}), 404
    return jsonify(store.to_dict()), 200


def delete(store_id: int):
    ok = store_service.delete_store(store_id)
    if not ok:
        return jsonify({"message": "Store not found"}), 404
    return jsonify({"message": "Store deleted"}), 200