from typing import List, Dict
from my_project.auth.dao import brand_products_dao


def get_all_links() -> List[Dict]:
    return brand_products_dao.get_all_links()


def get_products_for_brand(brand_id: int) -> List[Dict]:
    return brand_products_dao.get_products_for_brand(brand_id)


def get_brands_for_product(product_id: int) -> List[Dict]:
    return brand_products_dao.get_brands_for_product(product_id)


def create_link(data: dict) -> Dict:
    brand_id = data["brand_id"]
    product_id = data["product_id"]
    brand_products_dao.create_link(brand_id, product_id)
    return {"brand_id": brand_id, "product_id": product_id}


def delete_link(brand_id: int, product_id: int) -> bool:
    return brand_products_dao.delete_link(brand_id, product_id)