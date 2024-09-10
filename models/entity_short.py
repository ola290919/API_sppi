from typing import Optional

from models.default_model import DefaultModel
from pydantic import UUID4, Field


class EntityShort(DefaultModel):
    uuid: UUID4
    name: str
    from_date: Optional[int] = Field(default=None)  # TODO change to timestamp
    to_date: Optional[int] = Field(default=None)  # TODO change to timestamp
