from typing import List, Optional
from my_project.auth.dao.db import get_connection
from my_project.auth.domain.brand_website import BrandWebsite


def get_all_websites() -> List[BrandWebsite]:
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT website_id, brand_id, url FROM BrandWebsites")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [BrandWebsite.from_row(r) for r in rows]


def get_website_by_id(website_id: int) -> Optional[BrandWebsite]:
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute(
        "SELECT website_id, brand_id, url FROM BrandWebsites WHERE website_id = %s",
        (website_id,),
    )
    row = cur.fetchone()
    cur.close()
    conn.close()
    if not row:
        return None
    return BrandWebsite.from_row(row)


def create_website(website: BrandWebsite) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO BrandWebsites (brand_id, url) VALUES (%s, %s)",
        (website.brand_id, website.url),
    )
    conn.commit()
    new_id = cur.lastrowid
    cur.close()
    conn.close()
    return new_id


def update_website(website_id: int, website: BrandWebsite) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE BrandWebsites
        SET brand_id = %s, url = %s
        WHERE website_id = %s
        """,
        (website.brand_id, website.url, website_id),
    )
    conn.commit()
    updated = cur.rowcount > 0
    cur.close()
    conn.close()
    return updated


def delete_website(website_id: int) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM BrandWebsites WHERE website_id = %s", (website_id,))
    conn.commit()
    deleted = cur.rowcount > 0
    cur.close()
    conn.close()
    return deleted