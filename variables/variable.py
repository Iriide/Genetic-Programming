from exceptions import VariableTypeError
from types import SimpleType
from typing import Any


class Variable:
    value: Any
    declared: bool
    identifier: str
    type: SimpleType

    def __init__(self, identifier: str, variable_type: SimpleType):
        self.identifier = identifier
        self.type = variable_type
        self.declared = False
        self.value = None

    def on_declare(self):
        self.declared = True

    def on_assign(self, value: Any):
        try:
            self.type.value(value)
            self.value = self.type.value(value)
        except ValueError:
            raise VariableTypeError(self.identifier, self.type.name, value.__class__.__name__)