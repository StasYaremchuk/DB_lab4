from typing import List, Optional
from my_project.auth.dao import product_dao
from my_project.auth.domain.product import Product


def get_all_products() -> List[Product]:
    return product_dao.get_all_products()


def get_product(product_id: int) -> Optional[Product]:
    return product_dao.get_product_by_id(product_id)


def create_product(data: dict) -> Product:
    product = Product(
        product_id=None,
        product_name=data["product_name"],
        category_id=data["category_id"],
    )
    new_id = product_dao.create_product(product)
    product.product_id = new_id
    return product


def update_product(product_id: int, data: dict) -> Optional[Product]:
    product = product_dao.get_product_by_id(product_id)
    if product is None:
        return None

    if "product_name" in data:
        product.product_name = data["product_name"]
    if "category_id" in data:
        product.category_id = data["category_id"]

    ok = product_dao.update_product(product_id, product)
    if not ok:
        return None
    return product


def delete_product(product_id: int) -> bool:
    return product_dao.delete_product(product_id)