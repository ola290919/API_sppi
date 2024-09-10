from typing import List, Optional

from pydantic import RootModel, Field

from models.district_geometry import DistrictGeometry


class DistrictGeometryList(RootModel):
    root: List[Optional[DistrictGeometry]] = Field(default_factory=list)
