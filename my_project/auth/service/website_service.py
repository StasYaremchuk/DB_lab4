from typing import List, Optional
from my_project.auth.dao import website_dao
from my_project.auth.domain.brand_website import BrandWebsite


def get_all_websites() -> List[BrandWebsite]:
    return website_dao.get_all_websites()


def get_website(website_id: int) -> Optional[BrandWebsite]:
    return website_dao.get_website_by_id(website_id)


def create_website(data: dict) -> BrandWebsite:
    website = BrandWebsite(
        website_id=None,
        brand_id=data["brand_id"],
        url=data["url"],
    )
    new_id = website_dao.create_website(website)
    website.website_id = new_id
    return website


def update_website(website_id: int, data: dict) -> Optional[BrandWebsite]:
    website = website_dao.get_website_by_id(website_id)
    if website is None:
        return None

    if "brand_id" in data:
        website.brand_id = data["brand_id"]
    if "url" in data:
        website.url = data["url"]

    ok = website_dao.update_website(website_id, website)
    if not ok:
        return None
    return website


def delete_website(website_id: int) -> bool:
    return website_dao.delete_website(website_id)