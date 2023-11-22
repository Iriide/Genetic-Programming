from typing import Callable, Any
from variables.variable import Variable
from types_ import SimpleType


class InvalidTypeException(Exception):
    def __init__(self, left: Variable, right: Variable):
        super().__init__(f"Invalid type {left.type.name} and {right.type.name} for operation")


class NumericOnlyOperation:

    @staticmethod
    def SUBTRACTION(left: Any, right: Any) -> Any:
        return left - right

    @staticmethod
    def MULTIPLICATION(left: Any, right: Any) -> Any:
        return left * right

    @staticmethod
    def DIVISION(left: Any, right: Any) -> Any:
        return left / right

    @staticmethod
    def LESS_THAN_OR_EQUAL(left: Any, right: Any) -> Any:
        return left <= right

    @staticmethod
    def LESS_THAN(left: Any, right: Any) -> Any:
        return left < right

    @staticmethod
    def GREATER_THAN_OR_EQUAL(left: Any, right: Any) -> Any:
        return left >= right

    @staticmethod
    def GREATER_THAN(left: Any, right: Any) -> Any:
        return left > right


class BinaryOperationHandler:

    @staticmethod
    def addition_handler(left: Variable, right: Variable) -> int | float | str:
        VALID_TYPES = [SimpleType.INT, SimpleType.FLOAT, SimpleType.STRING]
        VALID_INTER_TYPE_OPERATIONS = {
            (SimpleType.INT, SimpleType.FLOAT): SimpleType.FLOAT,
            (SimpleType.FLOAT, SimpleType.INT): SimpleType.FLOAT,
            (SimpleType.INT, SimpleType.STRING): SimpleType.STRING,
            (SimpleType.STRING, SimpleType.INT): SimpleType.STRING,
            (SimpleType.FLOAT, SimpleType.STRING): SimpleType.STRING,
            (SimpleType.STRING, SimpleType.FLOAT): SimpleType.STRING,
        }

        if left.type == right.type and left.type in VALID_TYPES:
            return left.value + right.value

        if (left.type, right.type) in VALID_INTER_TYPE_OPERATIONS:
            return_type = VALID_INTER_TYPE_OPERATIONS[(left.type, right.type)]
            return return_type.value(left.value) + return_type.value(right.value)

        raise InvalidTypeException(left, right)

    @staticmethod
    def numeric_only_handler(left: Variable, right: Variable, bin_operation: Callable) -> int | float:

        VALID_TYPES = [SimpleType.INT, SimpleType.FLOAT]
        VALID_INTER_TYPE_OPERATIONS = {
            (SimpleType.INT, SimpleType.FLOAT): SimpleType.FLOAT,
            (SimpleType.FLOAT, SimpleType.INT): SimpleType.FLOAT,
        }

        if left.type == right.type and left.type in VALID_TYPES:
            return bin_operation(left.value, right.value)

        if (left.type, right.type) in VALID_INTER_TYPE_OPERATIONS:
            return_type = VALID_INTER_TYPE_OPERATIONS[(left.type, right.type)]
            return bin_operation(return_type.value(left.value), return_type.value(right.value))

        raise InvalidTypeException(left, right)

    @staticmethod
    def equality_handler(left: Variable, right: Variable) -> bool:
        VALID_TYPES = [SimpleType.INT, SimpleType.FLOAT, SimpleType.STRING, SimpleType.BOOL]

        if left.type == right.type and left.type in VALID_TYPES:
            return left.value == right.value

        if left.type == SimpleType.FLOAT and right.type == SimpleType.INT:
            return left.value == float(right.value)

        if left.type == SimpleType.INT and right.type == SimpleType.FLOAT:
            return float(left.value) == right.value

        raise InvalidTypeException(left, right)

    @staticmethod
    def inequality_handler(left: Variable, right: Variable) -> bool:
        return not BinaryOperationHandler.equality_handler(left, right)

    @staticmethod
    def logical_and_handler(left: Variable, right: Variable) -> bool:
        VALID_TYPES = [SimpleType.BOOL]

        if left.type == right.type and left.type in VALID_TYPES:
            return left.value and right.value

        raise InvalidTypeException(left, right)

    @staticmethod
    def logical_or_handler(left: Variable, right: Variable) -> bool:
        VALID_TYPES = [SimpleType.BOOL]

        if left.type == right.type and left.type in VALID_TYPES:
            return left.value or right.value

        raise InvalidTypeException(left, right)