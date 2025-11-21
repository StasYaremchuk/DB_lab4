from typing import List, Optional
from my_project.auth.dao import contact_dao
from my_project.auth.domain.store_contact import StoreContact


def get_all_contacts() -> List[StoreContact]:
    return contact_dao.get_all_contacts()


def get_contact(contact_id: int) -> Optional[StoreContact]:
    return contact_dao.get_contact_by_id(contact_id)


def create_contact(data: dict) -> StoreContact:
    contact = StoreContact(
        contact_id=None,
        store_id=data["store_id"],
        phone=data.get("phone"),
        email=data.get("email"),
    )
    new_id = contact_dao.create_contact(contact)
    contact.contact_id = new_id
    return contact


def update_contact(contact_id: int, data: dict) -> Optional[StoreContact]:
    contact = contact_dao.get_contact_by_id(contact_id)
    if contact is None:
        return None

    if "store_id" in data:
        contact.store_id = data["store_id"]
    if "phone" in data:
        contact.phone = data["phone"]
    if "email" in data:
        contact.email = data["email"]

    ok = contact_dao.update_contact(contact_id, contact)
    if not ok:
        return None
    return contact


def delete_contact(contact_id: int) -> bool:
    return contact_dao.delete_contact(contact_id)