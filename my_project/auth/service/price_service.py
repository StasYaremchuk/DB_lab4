from typing import List, Optional
from my_project.auth.dao import price_dao
from my_project.auth.domain.product_price import ProductPrice


def get_all_prices() -> List[ProductPrice]:
    return price_dao.get_all_prices()


def get_price(price_id: int) -> Optional[ProductPrice]:
    return price_dao.get_price_by_id(price_id)


def create_price(data: dict) -> ProductPrice:
    price = ProductPrice(
        price_id=None,
        product_id=data["product_id"],
        store_id=data["store_id"],
        price=data.get("price"),
    )
    new_id = price_dao.create_price(price)
    price.price_id = new_id
    return price


def update_price(price_id: int, data: dict) -> Optional[ProductPrice]:
    price_obj = price_dao.get_price_by_id(price_id)
    if price_obj is None:
        return None

    if "product_id" in data:
        price_obj.product_id = data["product_id"]
    if "store_id" in data:
        price_obj.store_id = data["store_id"]
    if "price" in data:
        price_obj.price = data["price"]

    ok = price_dao.update_price(price_id, price_obj)
    if not ok:
        return None
    return price_obj


def delete_price(price_id: int) -> bool:
    return price_dao.delete_price(price_id)