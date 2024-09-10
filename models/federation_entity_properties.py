from typing import Optional

from models.default_model import DefaultModel
from models.fields.country_code import CountryCode
from pydantic import UUID4, Field


class FederationEntityPropertiesGrid(DefaultModel):
    uuid: UUID4
    name: str


class FederationEntityProperties(FederationEntityPropertiesGrid):
    name_en: Optional[str] = Field(default=None)
    country_code: Optional[CountryCode] = Field(default=None)
    from_date: Optional[int] = Field(default=None)  # TODO change to timestamp
    to_date: Optional[int] = Field(default=None)  # TODO change to timestamp
