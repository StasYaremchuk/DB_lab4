from dataclasses import dataclass
from typing import Optional


@dataclass
class ProductPrice:
    price_id: Optional[int]
    product_id: int
    store_id: int
    price: Optional[float]

    @staticmethod
    def from_row(row: dict) -> "ProductPrice":
        return ProductPrice(
            price_id=row.get("price_id"),
            product_id=row.get("product_id"),
            store_id=row.get("store_id"),
            price=float(row["price"]) if row.get("price") is not None else None,
        )

    def to_dict(self) -> dict:
        return {
            "price_id": self.price_id,
            "product_id": self.product_id,
            "store_id": self.store_id,
            "price": self.price,
        }