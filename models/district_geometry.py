from typing import Optional

from pydantic import UUID4, Field

from models.default_model import DefaultModel
from models.fields.district_type_enum import DistrictTypeEnum
from models.level_limit import LevelLimit


class DistrictGeometry(DefaultModel):
    object_uuid: UUID4
    name: str
    type: DistrictTypeEnum
    object_parent_uuid: Optional[UUID4] = Field(default=None)
    name_en: Optional[str] = Field(default=None)
    lower_limit: Optional[LevelLimit] = Field(default=None)
    upper_limit: Optional[LevelLimit] = Field(default=None)
    geomWKB: bytes
    from_date: Optional[int] = Field(default=None)  # TODO change to timestamp
    to_date: Optional[int] = Field(default=None)  # TODO change to timestamp
    update_date: int  # TODO change to timestamp
