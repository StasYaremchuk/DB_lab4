from typing import List, Optional
from my_project.auth.dao.db import get_connection
from my_project.auth.domain.store_contact import StoreContact


def get_all_contacts() -> List[StoreContact]:
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT contact_id, store_id, phone, email FROM StoreContacts")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [StoreContact.from_row(r) for r in rows]


def get_contact_by_id(contact_id: int) -> Optional[StoreContact]:
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute(
        "SELECT contact_id, store_id, phone, email FROM StoreContacts WHERE contact_id = %s",
        (contact_id,),
    )
    row = cur.fetchone()
    cur.close()
    conn.close()
    if not row:
        return None
    return StoreContact.from_row(row)


def create_contact(contact: StoreContact) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO StoreContacts (store_id, phone, email) VALUES (%s, %s, %s)",
        (contact.store_id, contact.phone, contact.email),
    )
    conn.commit()
    new_id = cur.lastrowid
    cur.close()
    conn.close()
    return new_id


def update_contact(contact_id: int, contact: StoreContact) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE StoreContacts
        SET store_id = %s, phone = %s, email = %s
        WHERE contact_id = %s
        """,
        (contact.store_id, contact.phone, contact.email, contact_id),
    )
    conn.commit()
    updated = cur.rowcount > 0
    cur.close()
    conn.close()
    return updated


def delete_contact(contact_id: int) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM StoreContacts WHERE contact_id = %s", (contact_id,))
    conn.commit()
    deleted = cur.rowcount > 0
    cur.close()
    conn.close()
    return deleted