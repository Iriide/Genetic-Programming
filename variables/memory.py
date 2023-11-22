from exceptions import VariableNotDeclaredError, VariableAlreadyDeclaredError
from variables.variable import Variable
from types_ import SimpleType
from typing import Any
from utils.logger import createLogger
import logging


class VariableMemory:
    variables: dict[str, Variable]

    def __init__(self):
        self.variables = {}
        self.logger = createLogger("VariableMemory", logging.DEBUG)
        self.logger.info("Variable Memory initialized")

    def __del__(self):
        self.logger.info("Variable Memory deleting")
        self.logger.debug("-" * 30)
        self.logger.debug("Variable storage at end of program:")
        for variable in self.variables.values():
            self.logger.debug(f"{variable.identifier} = {variable.value} ({variable.type.name})")

    def declare_variable(self, identifier: str, variable_type: SimpleType):
        self.logger.debug(f"Declaration: {identifier} ({variable_type.name})")
        if identifier in self.variables:
            raise VariableAlreadyDeclaredError(identifier)
        self.variables[identifier] = Variable(identifier, variable_type)

    def assign_variable(self, identifier: str, value: Any):
        self.logger.debug(f"Assignment: {identifier} <- {value}")
        if identifier not in self.variables:
            raise VariableNotDeclaredError(identifier)
        self.variables[identifier].on_assign(value)

    def get_variable_value(self, identifier: str) -> Any:
        self.logger.debug(f"Get value: {identifier} -> {self.variables[identifier].value}")
        if identifier not in self.variables:
            raise VariableNotDeclaredError(identifier)
        return self.variables[identifier].value
