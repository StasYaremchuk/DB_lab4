from dataclasses import dataclass
from typing import Optional


@dataclass
class Brand:
    brand_id: Optional[int]
    brand_name: str
    description: Optional[str]

    @staticmethod
    def from_row(row: dict) -> "Brand":
        return Brand(
            brand_id=row.get("brand_id"),
            brand_name=row.get("brand_name"),
            description=row.get("description"),
        )

    def to_dict(self) -> dict:
        return {
            "brand_id": self.brand_id,
            "brand_name": self.brand_name,
            "description": self.description,
        }