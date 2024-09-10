from datetime import datetime
from typing import Optional

from models.default_model import DefaultModel
from models.details import Details, DetailsGrid
from models.federation_entity_properties import FederationEntityProperties, FederationEntityPropertiesGrid
from models.fields.country_code import CountryCode
from pydantic import UUID4, Field


class MunicipalSelf(DefaultModel):
    uuid: UUID4
    name: str
    name_en: Optional[str] = Field(default=None)
    country_code: Optional[CountryCode] = Field(default=None)
    from_date: Optional[int] = Field(default=None)  # TODO change to timestamp
    to_date: Optional[int] = Field(default=None)  # TODO change to timestamp
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = Field(default=None)
    created_by: str
    updated_by: str
    deleted_by: Optional[str] = Field(default=None)


class MunicipalDetail(MunicipalSelf):
    details: Details


class Municipal(MunicipalDetail):
    federal_entity: Optional[FederationEntityProperties] = Field(default=None)


class MunicipalGrid(MunicipalSelf):
    federal_entity: Optional[FederationEntityPropertiesGrid] = Field(default=None)
    details: DetailsGrid
