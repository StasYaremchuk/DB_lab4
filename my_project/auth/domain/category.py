from dataclasses import dataclass
from typing import Optional


@dataclass
class Category:
    category_id: Optional[int]
    category_name: str

    @staticmethod
    def from_row(row: dict) -> "Category":
        return Category(
            category_id=row.get("category_id"),
            category_name=row.get("category_name"),
        )

    def to_dict(self) -> dict:
        return {
            "category_id": self.category_id,
            "category_name": self.category_name,
        }