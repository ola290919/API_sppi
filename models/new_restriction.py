import random
from typing import Optional, Literal, List
from uuid import uuid4

import factory
from factory import SubFactory
from faker import Faker
from pydantic import Field

from models.default_model import DefaultModel
from models.document import Document, DocumentFactory


class NewRestriction(DefaultModel):
    object_uuid: str
    name: str
    restriction_type: Literal['whole', 'partial'] = Field(default='whole')
    state: Literal['limited', 'closed']
    from_date: Optional[int] = Field(default=None)
    to_date: Optional[int] = Field(default=None)
    comment: Optional[str] = Field(default=None)
    documents: Optional[List[Document]] = Field(default=None)


class NewRestrictionFactory(factory.Factory):
    class Meta:
        model = NewRestriction

    object_uuid = str(uuid4())
    name = factory.Faker('sentence', locale='ru_RU', nb_words=3)
    restriction_type = 'partial'  # со значением whole периодически вылетает 422 RESTRICTION_DATERANGE_CONFLICT
    state = random.choice(['limited', 'closed'])
    from_date: Optional[int] = factory.LazyFunction(
        lambda: int(Faker().date_time_this_year().timestamp()))
    to_date: Optional[int] = factory.LazyAttribute(
        lambda obj: obj.from_date + random.randint(0, 31536000))
    comment = factory.Faker('sentence')
    documents = factory.List([SubFactory(DocumentFactory)])
