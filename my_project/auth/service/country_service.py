from typing import List, Optional
from my_project.auth.dao import country_dao
from my_project.auth.domain.country import Country
from my_project.auth.domain.address import Address


def get_all_countries() -> List[Country]:
    return country_dao.get_all_countries()


def get_country(country_id: int) -> Optional[Country]:
    return country_dao.get_country_by_id(country_id)


def create_country(data: dict) -> Country:
    country = Country(country_id=None, country_name=data["country_name"])
    new_id = country_dao.create_country(country)
    country.country_id = new_id
    return country


def update_country(country_id: int, data: dict) -> Optional[Country]:
    country = country_dao.get_country_by_id(country_id)
    if country is None:
        return None

    if "country_name" in data:
        country.country_name = data["country_name"]

    updated = country_dao.update_country(country_id, country)
    if not updated:
        return None
    return country


def delete_country(country_id: int) -> bool:
    return country_dao.delete_country(country_id)


def get_addresses_for_country(country_id: int) -> List[Address]:
    return country_dao.get_addresses_for_country(country_id)


def get_all_countries_with_addresses():
    """
    Обгортка над DAO – повертає list[dict] для JOIN-запиту.
    """
    return country_dao.get_all_countries_with_addresses()