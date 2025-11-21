from typing import List, Optional
from my_project.auth.dao.db import get_connection
from my_project.auth.domain.category import Category


def get_all_categories() -> List[Category]:
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT category_id, category_name FROM Categories")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [Category.from_row(r) for r in rows]


def get_category_by_id(category_id: int) -> Optional[Category]:
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute(
        "SELECT category_id, category_name FROM Categories WHERE category_id = %s",
        (category_id,),
    )
    row = cur.fetchone()
    cur.close()
    conn.close()
    if not row:
        return None
    return Category.from_row(row)


def create_category(category: Category) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO Categories (category_name) VALUES (%s)",
        (category.category_name,),
    )
    conn.commit()
    new_id = cur.lastrowid
    cur.close()
    conn.close()
    return new_id


def update_category(category_id: int, category: Category) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE Categories SET category_name = %s WHERE category_id = %s",
        (category.category_name, category_id),
    )
    conn.commit()
    updated = cur.rowcount > 0
    cur.close()
    conn.close()
    return updated


def delete_category(category_id: int) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Categories WHERE category_id = %s", (category_id,))
    conn.commit()
    deleted = cur.rowcount > 0
    cur.close()
    conn.close()
    return deleted