from typing import List, Optional
from my_project.auth.dao.db import get_connection
from my_project.auth.domain.product import Product


def get_all_products() -> List[Product]:
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT product_id, product_name, category_id FROM Products")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [Product.from_row(r) for r in rows]


def get_product_by_id(product_id: int) -> Optional[Product]:
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute(
        "SELECT product_id, product_name, category_id FROM Products WHERE product_id = %s",
        (product_id,),
    )
    row = cur.fetchone()
    cur.close()
    conn.close()
    if not row:
        return None
    return Product.from_row(row)


def create_product(product: Product) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO Products (product_name, category_id) VALUES (%s, %s)",
        (product.product_name, product.category_id),
    )
    conn.commit()
    new_id = cur.lastrowid
    cur.close()
    conn.close()
    return new_id


def update_product(product_id: int, product: Product) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE Products
        SET product_name = %s, category_id = %s
        WHERE product_id = %s
        """,
        (product.product_name, product.category_id, product_id),
    )
    conn.commit()
    updated = cur.rowcount > 0
    cur.close()
    conn.close()
    return updated


def delete_product(product_id: int) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Products WHERE product_id = %s", (product_id,))
    conn.commit()
    deleted = cur.rowcount > 0
    cur.close()
    conn.close()
    return deleted