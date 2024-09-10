import random
from typing import Optional

import factory
from factory import SubFactory
from faker import Faker
from models.default_model import DefaultModel
from models.details import Details, DetailsFactory
from models.federation_entity import FederationEntity
from models.fields.country_code import CountryCode
from pydantic import Field


class NewMunicipal(DefaultModel):
    name: str
    name_en: Optional[str] = Field(default=None)
    country_code: Optional[CountryCode] = Field(default=None, examples=['RU'])
    from_date: Optional[int] = Field(default=None)  # TODO change to timestamp
    to_date: Optional[int] = Field(default=None)  # TODO change to timestamp
    federal_entity_uuid: str
    details: Details


class NewMunicipalFactory(factory.Factory):
    class Meta:
        model = NewMunicipal

    name = factory.Faker('city', locale='ru_RU')
    name_en = factory.Faker('city', locale='en_US')
    country_code = factory.Faker('country_code')
    from_date: Optional[int] = factory.LazyFunction(
        lambda: int(Faker().date_time_this_century().timestamp())
    )
    to_date: Optional[int] = factory.LazyAttribute(
        lambda obj: obj.from_date + random.randint(0, 31536000)  # Add up to 1 year in seconds
    )
    federal_entity_uuid = factory.LazyAttribute(
        lambda instance: str(FederationEntity.create().uuid)
    )
    details = SubFactory(DetailsFactory)
