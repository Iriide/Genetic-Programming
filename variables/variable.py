from exceptions import VariableTypeError
from simple_type import SimpleType, simple_type_from_generic_type
from typing import Any


class Variable:
    value: Any
    declared: bool
    identifier: str
    type: SimpleType

    def __init__(self, identifier: str, variable_type: SimpleType | Any):
        self.identifier = identifier
        if isinstance(variable_type, SimpleType):
            self.type = variable_type
        else:
            self.type = simple_type_from_generic_type(variable_type)
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

    def set_type(self, variable_type: SimpleType | Any):
        if isinstance(variable_type, SimpleType):
            self.type = variable_type
        else:
            self.type = simple_type_from_generic_type(variable_type)

    @staticmethod
    def create_and_assign(identifier: str, variable_type: SimpleType | Any, value: Any) -> "Variable":
        variable = Variable(identifier, variable_type)
        variable.on_declare()
        variable.on_assign(value)
        return variable
