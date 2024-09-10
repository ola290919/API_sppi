from datetime import datetime
from typing import Optional

from models.default_model import DefaultModel
from models.fields.country_code import CountryCode
from pydantic import UUID4, Field


class AerialPhotoGrid(DefaultModel):
    uuid: UUID4
    name: str
    from_date: Optional[int] = Field(default=None)  # TODO change to timestamp
    to_date: Optional[int] = Field(default=None)  # TODO change to timestamp
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = Field(default=None)
    created_by: str
    updated_by: str
    deleted_by: Optional[str] = Field(default=None)


class AerialPhoto(AerialPhotoGrid):
    name_en: Optional[str] = Field(default=None)
    country_code: Optional[CountryCode] = Field(default=None)
