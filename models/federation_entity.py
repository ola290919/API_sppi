from datetime import datetime
from typing import Optional

from models.default_model import DefaultModel
from models.details import Details, DetailsGrid
from models.fields.country_code import CountryCode
from models.new_federation_entity import NewFederationEntityFactory
from pydantic import UUID4, Field


class FederationEntitySelf(DefaultModel):
    uuid: UUID4
    name: str
    name_en: Optional[str] = Field(default=None)
    country_code: Optional[CountryCode] = Field(default=None)
    from_date: Optional[int] = Field(default=None)  # TODO change to timestamp
    to_date: Optional[int] = Field(default=None)  # TODO change to timestamp
    created_at: datetime
    updated_at: datetime
    created_by: str
    updated_by: str
    deleted_by: Optional[str] = Field(default=None)


class FederationEntity(FederationEntitySelf):
    details: Details

    @classmethod
    def create(cls, **kwargs):
        from utils.api_client import ApiClient
        api_client = ApiClient()

        response = api_client.as_admin().federation_entities().post(
            json=NewFederationEntityFactory.build(**kwargs).model_dump(mode='json'))

        return FederationEntity.model_validate(response.json())


class FederationEntityGrid(FederationEntitySelf):
    details: DetailsGrid
