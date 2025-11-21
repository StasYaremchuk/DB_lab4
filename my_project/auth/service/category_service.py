from typing import List, Optional
from my_project.auth.dao import category_dao
from my_project.auth.domain.category import Category


def get_all_categories() -> List[Category]:
    return category_dao.get_all_categories()


def get_category(category_id: int) -> Optional[Category]:
    return category_dao.get_category_by_id(category_id)


def create_category(data: dict) -> Category:
    category = Category(category_id=None, category_name=data["category_name"])
    new_id = category_dao.create_category(category)
    category.category_id = new_id
    return category


def update_category(category_id: int, data: dict) -> Optional[Category]:
    category = category_dao.get_category_by_id(category_id)
    if category is None:
        return None

    if "category_name" in data:
        category.category_name = data["category_name"]

    ok = category_dao.update_category(category_id, category)
    if not ok:
        return None
    return category


def delete_category(category_id: int) -> bool:
    return category_dao.delete_category(category_id)