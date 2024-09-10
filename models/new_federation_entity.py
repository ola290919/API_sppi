import random
from typing import Optional

import factory
from factory import SubFactory
from faker import Faker
from pydantic import Field

from models.default_model import DefaultModel
from models.details import Details, DetailsFactory
from models.fields.country_code import CountryCode


class NewFederationEntity(DefaultModel):
    name: str
    name_en: Optional[str] = Field(default=None)
    country_code: Optional[CountryCode] = Field(default=None, examples=['RU'])
    from_date: Optional[int] = Field(default=None)
    to_date: Optional[int] = Field(default=None)
    details: Details


class NewFederationEntityFactory(factory.Factory):
    class Meta:
        model = NewFederationEntity

    name = factory.Faker('city', locale='ru_RU')
    name_en = factory.Faker('city', locale='en_US')
    country_code = factory.LazyFunction(CountryCode.random)
    from_date: Optional[int] = factory.LazyFunction(
        lambda: int(Faker().date_time_this_century().timestamp())
    )
    to_date: Optional[int] = factory.LazyAttribute(
        lambda obj: obj.from_date + random.randint(0, 31536000)  # Add up to 1 year in seconds
    )
    details = SubFactory(DetailsFactory)
