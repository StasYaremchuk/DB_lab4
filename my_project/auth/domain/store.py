from dataclasses import dataclass
from typing import Optional


@dataclass
class Store:
    store_id: Optional[int]
    store_name: str
    brand_id: int
    address_id: int

    @staticmethod
    def from_row(row: dict) -> "Store":
        return Store(
            store_id=row.get("store_id"),
            store_name=row.get("store_name"),
            brand_id=row.get("brand_id"),
            address_id=row.get("address_id"),
        )

    def to_dict(self) -> dict:
        return {
            "store_id": self.store_id,
            "store_name": self.store_name,
            "brand_id": self.brand_id,
            "address_id": self.address_id,
        }