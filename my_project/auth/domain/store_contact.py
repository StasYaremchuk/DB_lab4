from dataclasses import dataclass
from typing import Optional


@dataclass
class StoreContact:
    contact_id: Optional[int]
    store_id: int
    phone: Optional[str]
    email: Optional[str]

    @staticmethod
    def from_row(row: dict) -> "StoreContact":
        return StoreContact(
            contact_id=row.get("contact_id"),
            store_id=row.get("store_id"),
            phone=row.get("phone"),
            email=row.get("email"),
        )

    def to_dict(self) -> dict:
        return {
            "contact_id": self.contact_id,
            "store_id": self.store_id,
            "phone": self.phone,
            "email": self.email,
        }