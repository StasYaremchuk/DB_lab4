from typing import List, Dict
from .db import get_connection


def get_all_links() -> List[Dict]:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT brand_id, product_id FROM BrandProducts ORDER BY brand_id, product_id"
    )
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows


def get_products_for_brand(brand_id: int) -> List[Dict]:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT
            p.product_id,
            p.product_name,
            p.category_id
        FROM BrandProducts bp
        JOIN Products p ON bp.product_id = p.product_id
        WHERE bp.brand_id = %s
        ORDER BY p.product_id
    """
    cursor.execute(query, (brand_id,))
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows


def get_brands_for_product(product_id: int) -> List[Dict]:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT
            b.brand_id,
            b.brand_name,
            b.description
        FROM BrandProducts bp
        JOIN Brands b ON bp.brand_id = b.brand_id
        WHERE bp.product_id = %s
        ORDER BY b.brand_id
    """
    cursor.execute(query, (product_id,))
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows


def create_link(brand_id: int, product_id: int) -> None:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO BrandProducts (brand_id, product_id) VALUES (%s, %s)",
        (brand_id, product_id),
    )
    conn.commit()

    cursor.close()
    conn.close()


def delete_link(brand_id: int, product_id: int) -> bool:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM BrandProducts WHERE brand_id = %s AND product_id = %s",
        (brand_id, product_id),
    )
    conn.commit()
    deleted = cursor.rowcount > 0

    cursor.close()
    conn.close()
    return deleted