from typing import Optional, List

import factory
from factory import SubFactory
from pydantic import Field

from models.contact_data import ContactData, ContactDataFactory
from models.default_model import DefaultModel
from models.mailing_address import MailingAddress, MailingAddressFactory


class PatchDetails(DefaultModel):
    registered_in_sppi: Optional[bool] = Field(default=None)
    head_full_name: Optional[str] = Field(default=None)
    actual_address: Optional[str] = Field(default=None)
    legal_address: Optional[str] = Field(default=None)
    phone: Optional[str] = Field(default=None)
    email: Optional[str] = Field(default=None)
    contact: Optional[ContactData] = Field(default=None)
    mailing_addresses: Optional[List[MailingAddress]]


class PatchDetailsFactory(factory.Factory):
    class Meta:
        model = PatchDetails

    registered_in_sppi: Optional[bool] = factory.Faker('boolean')
    head_full_name: Optional[str] = factory.Faker('name', locale='ru_RU')
    actual_address: Optional[str] = factory.Faker('address', locale='ru_RU')
    legal_address: Optional[str] = factory.Faker('address', locale='ru_RU')
    phone: Optional[str] = factory.Faker('phone_number')
    email: Optional[str] = factory.Faker('email')
    contact: Optional[ContactData] = SubFactory(ContactDataFactory)
    mailing_addresses: Optional[List[MailingAddress]] = factory.List([SubFactory(MailingAddressFactory)])
