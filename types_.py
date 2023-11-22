from enum import Enum


class SimpleType(Enum):
    INT = int
    FLOAT = float
    STRING = str
    BOOL = bool


def get_simple_type(type_obj) -> SimpleType:
    if type_obj == int:
        return SimpleType.INT
    elif type_obj == float:
        return SimpleType.FLOAT
    elif type_obj == str:
        return SimpleType.STRING
    elif type_obj == bool:
        return SimpleType.BOOL
    else:
        raise ValueError(f"Invalid type {type_obj}")