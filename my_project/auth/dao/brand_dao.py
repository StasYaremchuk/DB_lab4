from typing import List, Optional
from my_project.auth.dao.db import get_connection
from my_project.auth.domain.brand import Brand


def get_all_brands() -> List[Brand]:
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT brand_id, brand_name, description FROM Brands")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [Brand.from_row(r) for r in rows]


def get_brand_by_id(brand_id: int) -> Optional[Brand]:
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute(
        "SELECT brand_id, brand_name, description FROM Brands WHERE brand_id = %s",
        (brand_id,),
    )
    row = cur.fetchone()
    cur.close()
    conn.close()
    if not row:
        return None
    return Brand.from_row(row)


def create_brand(brand: Brand) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO Brands (brand_name, description) VALUES (%s, %s)",
        (brand.brand_name, brand.description),
    )
    conn.commit()
    new_id = cur.lastrowid
    cur.close()
    conn.close()
    return new_id


def update_brand(brand_id: int, brand: Brand) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE Brands SET brand_name=%s, description=%s WHERE brand_id=%s",
        (brand.brand_name, brand.description, brand_id),
    )
    conn.commit()
    updated = cur.rowcount > 0
    cur.close()
    conn.close()
    return updated


def delete_brand(brand_id: int) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Brands WHERE brand_id=%s", (brand_id,))
    conn.commit()
    deleted = cur.rowcount > 0
    cur.close()
    conn.close()
    return deleted