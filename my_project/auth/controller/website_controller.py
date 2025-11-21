from flask import jsonify, request
from my_project.auth.service import website_service


def get_all():
    websites = website_service.get_all_websites()
    return jsonify([w.to_dict() for w in websites]), 200


def get_one(website_id: int):
    website = website_service.get_website(website_id)
    if website is None:
        return jsonify({"message": "Website not found"}), 404
    return jsonify(website.to_dict()), 200


def create():
    data = request.get_json() or {}
    required = ("brand_id", "url")
    if not all(k in data for k in required):
        return jsonify({"message": "brand_id and url are required"}), 400

    website = website_service.create_website(data)
    return jsonify(website.to_dict()), 201


def update(website_id: int):
    data = request.get_json() or {}
    website = website_service.update_website(website_id, data)
    if website is None:
        return jsonify({"message": "Website not found"}), 404
    return jsonify(website.to_dict()), 200


def delete(website_id: int):
    ok = website_service.delete_website(website_id)
    if not ok:
        return jsonify({"message": "Website not found"}), 404
    return jsonify({"message": "Website deleted"}), 200