from typing import Optional

import factory
from pydantic import Field

from models.default_model import DefaultModel


class MailingAddress(DefaultModel):
    code: Optional[str] = Field(default=None)
    address: Optional[str] = Field(default=None)


class MailingAddressFactory(factory.Factory):
    class Meta:
        model = MailingAddress

    code = factory.Faker('postcode')
    address = factory.Faker('address', locale='ru_RU')
