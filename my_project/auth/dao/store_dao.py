from typing import List, Optional
from my_project.auth.dao.db import get_connection
from my_project.auth.domain.store import Store


def get_all_stores() -> List[Store]:
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT store_id, store_name, brand_id, address_id FROM Stores")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [Store.from_row(r) for r in rows]


def get_store_by_id(store_id: int) -> Optional[Store]:
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute(
        "SELECT store_id, store_name, brand_id, address_id FROM Stores WHERE store_id = %s",
        (store_id,),
    )
    row = cur.fetchone()
    cur.close()
    conn.close()
    if not row:
        return None
    return Store.from_row(row)


def create_store(store: Store) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO Stores (store_name, brand_id, address_id) VALUES (%s, %s, %s)",
        (store.store_name, store.brand_id, store.address_id),
    )
    conn.commit()
    new_id = cur.lastrowid
    cur.close()
    conn.close()
    return new_id


def update_store(store_id: int, store: Store) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE Stores
        SET store_name = %s, brand_id = %s, address_id = %s
        WHERE store_id = %s
        """,
        (store.store_name, store.brand_id, store.address_id, store_id),
    )
    conn.commit()
    updated = cur.rowcount > 0
    cur.close()
    conn.close()
    return updated


def delete_store(store_id: int) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Stores WHERE store_id = %s", (store_id,))
    conn.commit()
    deleted = cur.rowcount > 0
    cur.close()
    conn.close()
    return deleted