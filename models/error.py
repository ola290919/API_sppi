from typing import Optional

from pydantic import Field

from models.default_model import DefaultModel


class Error(DefaultModel):
    type: Optional[str] = Field(default=None)
    title: Optional[str] = Field(default=None)
    status: Optional[str] = Field(default=None)
    detail: Optional[str] = Field(default=None)
    instance: Optional[str] = Field(default=None)
