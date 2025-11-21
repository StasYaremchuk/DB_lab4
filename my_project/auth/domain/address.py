from dataclasses import dataclass
from typing import Optional


@dataclass
class Address:
    address_id: Optional[int]
    country_id: int
    city: Optional[str]
    street: Optional[str]

    @staticmethod
    def from_row(row: dict) -> "Address":
        return Address(
            address_id=row.get("address_id"),
            country_id=row.get("country_id"),
            city=row.get("city"),
            street=row.get("street"),
        )

    def to_dict(self) -> dict:
        return {
            "address_id": self.address_id,
            "country_id": self.country_id,
            "city": self.city,
            "street": self.street,
        }