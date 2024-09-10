import factory
from pydantic import RootModel, Field


class LevelValue(RootModel):
    root: str = Field(..., max_length=6)


class LevelValueFactory(factory.Factory):
    class Meta:
        model = LevelValue

    @classmethod
    def _build(cls, model_class, *args, **kwargs):
        return LevelValue(root='S0335')
