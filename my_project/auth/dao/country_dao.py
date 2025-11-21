from typing import List, Optional
from .db import get_connection
from my_project.auth.domain.country import Country
from my_project.auth.domain.address import Address


def get_all_countries() -> List[Country]:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT country_id, country_name FROM Countries")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return [Country(**row) for row in rows]


def get_country_by_id(country_id: int) -> Optional[Country]:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT country_id, country_name FROM Countries WHERE country_id = %s",
        (country_id,),
    )
    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if row is None:
        return None
    return Country(**row)


def create_country(country: Country) -> int:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO Countries (country_name) VALUES (%s)",
        (country.country_name,),
    )
    conn.commit()
    new_id = cursor.lastrowid

    cursor.close()
    conn.close()
    return new_id


def update_country(country_id: int, country: Country) -> bool:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE Countries SET country_name = %s WHERE country_id = %s",
        (country.country_name, country_id),
    )
    conn.commit()
    updated = cursor.rowcount > 0

    cursor.close()
    conn.close()
    return updated


def delete_country(country_id: int) -> bool:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Countries WHERE country_id = %s", (country_id,))
    conn.commit()
    deleted = cursor.rowcount > 0

    cursor.close()
    conn.close()
    return deleted


def get_addresses_for_country(country_id: int) -> List[Address]:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT address_id, country_id, city, street
        FROM Addresses
        WHERE country_id = %s
        """,
        (country_id,),
    )
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return [Address(**row) for row in rows]


def get_all_countries_with_addresses():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT
            c.country_id,
            c.country_name,
            a.address_id,
            a.city,
            a.street
        FROM Countries c
        LEFT JOIN Addresses a ON c.country_id = a.country_id
        ORDER BY c.country_id, a.address_id
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows