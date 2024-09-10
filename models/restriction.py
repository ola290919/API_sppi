from datetime import datetime
from typing import Optional, Literal, List

from pydantic import UUID4, Field

from models.default_model import DefaultModel
from models.document import Document


class Restriction(DefaultModel):
    uuid: UUID4
    object_uuid: UUID4
    name: str
    restriction_type: Literal['whole', 'partial'] = Field(default='whole')
    state: Literal['limited', 'closed']
    from_date: Optional[int] = Field(default=None)
    to_date: Optional[int] = Field(default=None)
    comment: Optional[str] = Field(default=None)
    documents: Optional[List[Document]] = Field(default=None)
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = Field(default=None)
    created_by: str
    updated_by: str
    deleted_by: Optional[str] = Field(default=None)
