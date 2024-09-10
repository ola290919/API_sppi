from typing import List, Optional

from pydantic import Field, RootModel, UUID4


class RestrictionsUpdatesList(RootModel):
    root: List[Optional[UUID4]] = Field(default_factory=list)
