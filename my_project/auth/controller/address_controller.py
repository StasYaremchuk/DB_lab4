from flask import jsonify, request
from my_project.auth.service import address_service


def get_all():
    addresses = address_service.get_all_addresses()
    return jsonify([a.to_dict() for a in addresses]), 200


def get_one(address_id: int):
    address = address_service.get_address(address_id)
    if address is None:
        return jsonify({"message": "Address not found"}), 404
    return jsonify(address.to_dict()), 200


def create():
    data = request.get_json() or {}
    required = ("country_id",)
    if not all(k in data for k in required):
        return jsonify({"message": "country_id is required"}), 400

    address = address_service.create_address(data)
    return jsonify(address.to_dict()), 201


def update(address_id: int):
    data = request.get_json() or {}
    address = address_service.update_address(address_id, data)
    if address is None:
        return jsonify({"message": "Address not found"}), 404
    return jsonify(address.to_dict()), 200


def delete(address_id: int):
    ok = address_service.delete_address(address_id)
    if not ok:
        return jsonify({"message": "Address not found"}), 404
    return jsonify({"message": "Address deleted"}), 200