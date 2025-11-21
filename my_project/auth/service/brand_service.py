from typing import List, Optional
from my_project.auth.dao import brand_dao
from my_project.auth.domain.brand import Brand


def get_all_brands() -> List[Brand]:
    return brand_dao.get_all_brands()


def get_brand(brand_id: int) -> Optional[Brand]:
    return brand_dao.get_brand_by_id(brand_id)


def create_brand(data: dict) -> Brand:
    brand = Brand(
        brand_id=None,
        brand_name=data["brand_name"],
        description=data.get("description"),
    )
    new_id = brand_dao.create_brand(brand)
    brand.brand_id = new_id
    return brand


def update_brand(brand_id: int, data: dict) -> Optional[Brand]:
    brand = brand_dao.get_brand_by_id(brand_id)
    if brand is None:
        return None

    if "brand_name" in data:
        brand.brand_name = data["brand_name"]
    if "description" in data:
        brand.description = data["description"]

    ok = brand_dao.update_brand(brand_id, brand)
    if not ok:
        return None
    return brand


def delete_brand(brand_id: int) -> bool:
    return brand_dao.delete_brand(brand_id)