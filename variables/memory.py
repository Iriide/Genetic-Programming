from exceptions import VariableNotDeclaredError, VariableAlreadyDeclaredError
from variable import Variable
from types import SimpleType
from typing import Any


class VariableMemory:
    variables: dict[str, Variable]

    def __init__(self):
        self.variables = {}

    def __del__(self):
        print("Variable storage at end of program:")
        for variable in self.variables.values():
            print(f"{variable.identifier} = {variable.value} ({variable.type.name})")

    def declare_variable(self, identifier: str, variable_type: SimpleType):
        if identifier in self.variables:
            raise VariableAlreadyDeclaredError(identifier)
        self.variables[identifier] = Variable(identifier, variable_type)

    def assign_variable(self, identifier: str, value: Any):
        if identifier not in self.variables:
            raise VariableNotDeclaredError(identifier)
        self.variables[identifier].on_assign(value)

    def get_variable(self, identifier: str) -> Variable:
        if identifier not in self.variables:
            raise VariableNotDeclaredError(identifier)
        return self.variables[identifier]

    def get_variable_value(self, identifier: str) -> Any:
        if identifier not in self.variables:
            raise VariableNotDeclaredError(identifier)
        return self.variables[identifier].value
