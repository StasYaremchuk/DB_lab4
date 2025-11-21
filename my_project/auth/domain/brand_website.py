from dataclasses import dataclass
from typing import Optional


@dataclass
class BrandWebsite:
    website_id: Optional[int]
    brand_id: int
    url: str

    @staticmethod
    def from_row(row: dict) -> "BrandWebsite":
        return BrandWebsite(
            website_id=row.get("website_id"),
            brand_id=row.get("brand_id"),
            url=row.get("url"),
        )

    def to_dict(self) -> dict:
        return {
            "website_id": self.website_id,
            "brand_id": self.brand_id,
            "url": self.url,
        }