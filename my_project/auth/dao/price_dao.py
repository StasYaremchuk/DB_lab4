from typing import List, Optional
from my_project.auth.dao.db import get_connection
from my_project.auth.domain.product_price import ProductPrice


def get_all_prices() -> List[ProductPrice]:
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT price_id, product_id, store_id, price FROM ProductPrices")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [ProductPrice.from_row(r) for r in rows]


def get_price_by_id(price_id: int) -> Optional[ProductPrice]:
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute(
        "SELECT price_id, product_id, store_id, price FROM ProductPrices WHERE price_id = %s",
        (price_id,),
    )
    row = cur.fetchone()
    cur.close()
    conn.close()
    if not row:
        return None
    return ProductPrice.from_row(row)


def create_price(price: ProductPrice) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO ProductPrices (product_id, store_id, price) VALUES (%s, %s, %s)",
        (price.product_id, price.store_id, price.price),
    )
    conn.commit()
    new_id = cur.lastrowid
    cur.close()
    conn.close()
    return new_id


def update_price(price_id: int, price: ProductPrice) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE ProductPrices
        SET product_id = %s, store_id = %s, price = %s
        WHERE price_id = %s
        """,
        (price.product_id, price.store_id, price.price, price_id),
    )
    conn.commit()
    updated = cur.rowcount > 0
    cur.close()
    conn.close()
    return updated


def delete_price(price_id: int) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM ProductPrices WHERE price_id = %s", (price_id,))
    conn.commit()
    deleted = cur.rowcount > 0
    cur.close()
    conn.close()
    return deleted