from dataclasses import dataclass


@dataclass
class BrandProduct:
    brand_id: int
    product_id: int

    def to_dict(self) -> dict:
        return {
            "brand_id": self.brand_id,
            "product_id": self.product_id,
        }