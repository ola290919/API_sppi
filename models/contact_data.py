from typing import Optional

import factory
from pydantic import Field

from models.default_model import DefaultModel


class ContactData(DefaultModel):
    full_name: Optional[str] = Field(default=None)
    phone: Optional[str] = Field(default=None)
    email: Optional[str] = Field(default=None)


class ContactDataFactory(factory.Factory):
    class Meta:
        model = ContactData

    full_name = factory.Faker('name', locale='ru_RU')
    phone = factory.Faker('phone_number')
    email = factory.Faker('email')
