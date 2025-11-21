from dataclasses import dataclass
from typing import Optional


@dataclass
class Product:
    product_id: Optional[int]
    product_name: str
    category_id: int

    @staticmethod
    def from_row(row: dict) -> "Product":
        return Product(
            product_id=row.get("product_id"),
            product_name=row.get("product_name"),
            category_id=row.get("category_id"),
        )

    def to_dict(self) -> dict:
        return {
            "product_id": self.product_id,
            "product_name": self.product_name,
            "category_id": self.category_id,
        }