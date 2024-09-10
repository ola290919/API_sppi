from pydantic import BaseModel, ConfigDict


class DefaultModel(BaseModel):
    model_config = ConfigDict(extra='forbid')
