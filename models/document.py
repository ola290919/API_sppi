from typing import Optional

import factory
from pydantic import Field

from models.default_model import DefaultModel


class Document(DefaultModel):
    short_name: Optional[str] = Field(default=None)
    full_name: Optional[str] = Field(default=None)
    document_link: Optional[str] = Field(default=None)
    internal_file_id: Optional[str] = Field(default=None)


class DocumentFactory(factory.Factory):
    class Meta:
        model = Document

    short_name = factory.Faker('file_name')
    full_name = factory.Faker('file_name')
    document_link = factory.Faker('url')
    internal_file_id = factory.Faker('uuid4')
