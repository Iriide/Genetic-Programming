class VariableNotDeclaredError(Exception):
    def __init__(self, identifier: str):
        super().__init__(f"Variable {identifier} not declared")


class VariableAlreadyDeclaredError(Exception):
    def __init__(self, identifier: str):
        super().__init__(f"Variable {identifier} already declared")


class VariableTypeError(Exception):
    def __init__(self, identifier: str, expected_type: str, actual_type: str):
        super().__init__(f"Variable {identifier} expected type {expected_type}, got {actual_type}")
