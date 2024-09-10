from enum import Enum


class LevelUnitEnum(str, Enum):
    TABLE = "table"
    MQNE = "mqne"
    FTQNE = "ftqne"
    MAMSL = "mamsl"
    FTAMSL = "ftamsl"
    MAGL = "magl"
    FTAGL = "ftagl"
    GND = "gnd"
    UNL = "unl"
    FL = "fl"
