from flask import jsonify, request
from my_project.auth.service import country_service


def get_all():
    countries = country_service.get_all_countries()
    return jsonify([c.to_dict() for c in countries]), 200


def get_one(country_id: int):
    country = country_service.get_country(country_id)
    if country is None:
        return jsonify({"message": "Country not found"}), 404
    return jsonify(country.to_dict()), 200


def create():
    data = request.get_json() or {}
    if "country_name" not in data:
        return jsonify({"message": "country_name is required"}), 400

    country = country_service.create_country(data)
    return jsonify(country.to_dict()), 201


def update(country_id: int):
    data = request.get_json() or {}
    country = country_service.update_country(country_id, data)
    if country is None:
        return jsonify({"message": "Country not found"}), 404
    return jsonify(country.to_dict()), 200


def delete(country_id: int):
    ok = country_service.delete_country(country_id)
    if not ok:
        return jsonify({"message": "Country not found"}), 404
    return jsonify({"message": "Country deleted"}), 200


def get_addresses(country_id: int):
    """
    M:1 – адреси конкретної країни
    """
    country = country_service.get_country(country_id)
    if country is None:
        return jsonify({"message": "Country not found"}), 404

    addresses = country_service.get_addresses_for_country(country_id)
    return jsonify([a.to_dict() for a in addresses]), 200


def get_all_with_addresses():
    rows = country_service.get_all_countries_with_addresses()
    return jsonify(rows), 200