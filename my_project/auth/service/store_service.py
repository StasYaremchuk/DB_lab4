from typing import List, Optional
from my_project.auth.dao import store_dao
from my_project.auth.domain.store import Store


def get_all_stores() -> List[Store]:
    return store_dao.get_all_stores()


def get_store(store_id: int) -> Optional[Store]:
    return store_dao.get_store_by_id(store_id)


def create_store(data: dict) -> Store:
    store = Store(
        store_id=None,
        store_name=data["store_name"],
        brand_id=data["brand_id"],
        address_id=data["address_id"],
    )
    new_id = store_dao.create_store(store)
    store.store_id = new_id
    return store


def update_store(store_id: int, data: dict) -> Optional[Store]:
    store = store_dao.get_store_by_id(store_id)
    if store is None:
        return None

    if "store_name" in data:
        store.store_name = data["store_name"]
    if "brand_id" in data:
        store.brand_id = data["brand_id"]
    if "address_id" in data:
        store.address_id = data["address_id"]

    ok = store_dao.update_store(store_id, store)
    if not ok:
        return None
    return store


def delete_store(store_id: int) -> bool:
    return store_dao.delete_store(store_id)