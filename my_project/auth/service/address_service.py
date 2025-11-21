from typing import List, Optional
from my_project.auth.dao import address_dao
from my_project.auth.domain.address import Address


def get_all_addresses() -> List[Address]:
    return address_dao.get_all_addresses()


def get_address(address_id: int) -> Optional[Address]:
    return address_dao.get_address_by_id(address_id)


def create_address(data: dict) -> Address:
    address = Address(
        address_id=None,
        country_id=data["country_id"],
        city=data.get("city"),
        street=data.get("street"),
    )
    new_id = address_dao.create_address(address)
    address.address_id = new_id
    return address


def update_address(address_id: int, data: dict) -> Optional[Address]:
    address = address_dao.get_address_by_id(address_id)
    if address is None:
        return None

    if "country_id" in data:
        address.country_id = data["country_id"]
    if "city" in data:
        address.city = data["city"]
    if "street" in data:
        address.street = data["street"]

    ok = address_dao.update_address(address_id, address)
    if not ok:
        return None
    return address


def delete_address(address_id: int) -> bool:
    return address_dao.delete_address(address_id)