from typing import List, Optional
from my_project.auth.dao.db import get_connection
from my_project.auth.domain.address import Address


def get_all_addresses() -> List[Address]:
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT address_id, country_id, city, street FROM Addresses")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [Address.from_row(r) for r in rows]


def get_address_by_id(address_id: int) -> Optional[Address]:
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute(
        "SELECT address_id, country_id, city, street FROM Addresses WHERE address_id = %s",
        (address_id,),
    )
    row = cur.fetchone()
    cur.close()
    conn.close()
    if not row:
        return None
    return Address.from_row(row)


def create_address(address: Address) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO Addresses (country_id, city, street) VALUES (%s, %s, %s)",
        (address.country_id, address.city, address.street),
    )
    conn.commit()
    new_id = cur.lastrowid
    cur.close()
    conn.close()
    return new_id


def update_address(address_id: int, address: Address) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE Addresses
        SET country_id = %s, city = %s, street = %s
        WHERE address_id = %s
        """,
        (address.country_id, address.city, address.street, address_id),
    )
    conn.commit()
    updated = cur.rowcount > 0
    cur.close()
    conn.close()
    return updated


def delete_address(address_id: int) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Addresses WHERE address_id = %s", (address_id,))
    conn.commit()
    deleted = cur.rowcount > 0
    cur.close()
    conn.close()
    return deleted