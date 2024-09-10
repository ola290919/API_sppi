import factory

from models.default_model import DefaultModel
from models.fields.level_unit_enum import LevelUnitEnum
from models.fields.level_value import LevelValue, LevelValueFactory


class LevelLimit(DefaultModel):
    unit: LevelUnitEnum
    value: LevelValue


class LevelLimitFactory(factory.Factory):
    class Meta:
        model = LevelLimit

    unit = LevelUnitEnum.TABLE
    value = factory.SubFactory(LevelValueFactory)
