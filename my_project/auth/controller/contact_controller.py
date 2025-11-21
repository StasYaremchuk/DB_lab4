from flask import jsonify, request
from my_project.auth.service import contact_service


def get_all():
    contacts = contact_service.get_all_contacts()
    return jsonify([c.to_dict() for c in contacts]), 200


def get_one(contact_id: int):
    contact = contact_service.get_contact(contact_id)
    if contact is None:
        return jsonify({"message": "Contact not found"}), 404
    return jsonify(contact.to_dict()), 200


def create():
    data = request.get_json() or {}
    if "store_id" not in data:
        return jsonify({"message": "store_id is required"}), 400

    contact = contact_service.create_contact(data)
    return jsonify(contact.to_dict()), 201


def update(contact_id: int):
    data = request.get_json() or {}
    contact = contact_service.update_contact(contact_id, data)
    if contact is None:
        return jsonify({"message": "Contact not found"}), 404
    return jsonify(contact.to_dict()), 200


def delete(contact_id: int):
    ok = contact_service.delete_contact(contact_id)
    if not ok:
        return jsonify({"message": "Contact not found"}), 404
    return jsonify({"message": "Contact deleted"}), 200