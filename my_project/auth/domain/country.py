from dataclasses import dataclass
from typing import Optional


@dataclass
class Country:
    country_id: Optional[int]
    country_name: str

    @staticmethod
    def from_row(row: dict) -> "Country":
        return Country(
            country_id=row.get("country_id"),
            country_name=row.get("country_name"),
        )

    def to_dict(self) -> dict:
        return {
            "country_id": self.country_id,
            "country_name": self.country_name,
        }