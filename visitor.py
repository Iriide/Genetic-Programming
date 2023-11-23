import logging

import utils.logger
from binary_operation_handler import BinaryOperationHandler, NumericOnlyOperation
from gen.MiniLanguageParserVisitor import MiniLanguageParserVisitor
from gen.MiniLanguageParser import MiniLanguageParser
from simple_type import SimpleType
from typing import TextIO

from variables.memory import VariableMemory
from variables.variable import Variable


class InterpreterVisitor(MiniLanguageParserVisitor):
    in_file: TextIO
    out_file: TextIO
    variable_memory: VariableMemory

    def __init__(self, in_path: str, out_path: str):
        super().__init__()
        self.logger = utils.logger.createLogger("Visitor", logging.DEBUG)
        self.logger.info("Visitor initialized")
        self.in_file = open(in_path, "r")
        self.out_file = open(out_path, "w+")
        self.variable_memory = VariableMemory()

    def __del__(self):
        self.in_file.close()
        self.out_file.close()

    def visitProgram(self, ctx: MiniLanguageParser.ProgramContext):
        self.visitChildren(ctx)

    def visitBlock(self, ctx: MiniLanguageParser.BlockContext):
        self.visitChildren(ctx)

    def visitStatement(self, ctx: MiniLanguageParser.StatementContext):
        for child in ctx.children:
            self.visit(child)

    def visitDeclStatement(self, ctx: MiniLanguageParser.DeclStatementContext):
        variable_type = SimpleType[ctx.typeSpecifier().getText().upper()]
        # Go through all the declarations
        for decl_context in ctx.declWithOptionalAssignment():
            identifier = decl_context.identifier().getText()
            self.variable_memory.declare_variable(identifier, variable_type)
            # If there is an assignment, assign the value
            if decl_context.expression():
                value = self.visit(decl_context.expression())
                self.variable_memory.assign_variable(identifier, value)

    def visitAssignmentStatement(self, ctx: MiniLanguageParser.AssignmentStatementContext):
        identifier = ctx.identifier().getText()
        value = self.visit(ctx.expression())
        self.variable_memory.assign_variable(identifier, value)

    def visitDeclWithOptionalAssignment(self, ctx: MiniLanguageParser.DeclWithOptionalAssignmentContext):
        identifier = ctx.identifier().getText()
        if ctx.expression():
            value = self.visit(ctx.expression())
            self.variable_memory.assign_variable(identifier, value)

        else:
            self.variable_memory.declare_variable(identifier, SimpleType[ctx.expression().typeSpecifier().getText()])

    def visitIfStatement(self, ctx: MiniLanguageParser.IfStatementContext):
        # check if there is an else statement
        if ctx.KW_ELSE():
            # iterate through the conditions and statements without the last statement (which is the else statement)
            for condition, statement in zip(ctx.expression(), ctx.statement()[:-1]):
                if self.visit(condition):
                    self.visit(statement)
                    break

                self.visit(ctx.statement()[-1])

        else:
            # iterate through the conditions and statements
            for condition, statement in zip(ctx.expression(), ctx.statement()):
                if self.visit(condition):
                    self.visit(statement)
                    break

    def visitLoopStatement(self, ctx: MiniLanguageParser.LoopStatementContext):
        while self.visit(ctx.expression()):
            self.visit(ctx.statement())

    def visitRead(self, ctx: MiniLanguageParser.ReadContext):
        self.logger.debug("Reading from file: " + ctx.identifier().getText())
        identifier = ctx.identifier().getText()
        value = self.in_file.readline()
        self.variable_memory.assign_variable(identifier, value)

    def visitWrite(self, ctx: MiniLanguageParser.WriteContext):
        self.logger.debug("Writing to file: " + ctx.expression().getText())
        value = self.visit(ctx.expression())
        self.out_file.write(str(value) + "\n")

    def visitExpression(self, ctx: MiniLanguageParser.ExpressionContext):
        return self.visitChildren(ctx)

    def visitPrimaryExpression(self, ctx: MiniLanguageParser.PrimaryExpressionContext):
        if ctx.identifier():
            return self.variable_memory.get_variable_value(ctx.identifier().getText())
        elif ctx.literal():
            if ctx.literal().INTEGER_LITERAL():
                return int(ctx.literal().getText())
            elif ctx.literal().FLOAT_LITERAL():
                return float(ctx.literal().getText())
            elif ctx.literal().STRING_LITERAL():
                return str(ctx.literal().getText().replace('"', '').replace("\\n", "\n"))
            elif ctx.literal().BOOL_LITERAL():
                if ctx.literal().getText() == "true":
                    return True
                elif ctx.literal().getText() == "false":
                    return False

    def visitUnaryExpression(self, ctx: MiniLanguageParser.UnaryExpressionContext):
        if ctx.unaryOperator():
            value = self.visit(ctx.unaryExpression())
            if ctx.unaryOperator().MINUS():
                return -value
            elif ctx.unaryOperator().NOT():
                return not value
            else:
                return value
        return self.visit(ctx.primaryExpression())

    def visitMultiplicativeExpression(self, ctx: MiniLanguageParser.MultiplicativeExpressionContext):
        value = self.visit(ctx.unaryExpression()[0])

        for expression in range(1, len(ctx.unaryExpression())):
            if ctx.TIMES():
                value *= self.visit(ctx.unaryExpression()[expression])
            elif ctx.DIV() and self.visit(ctx.unaryExpression()[expression]) != 0:
                value /= self.visit(ctx.unaryExpression()[expression])

        return value

    def visitAdditiveExpression(self, ctx: MiniLanguageParser.AdditiveExpressionContext):
        if len(ctx.multiplicativeExpression()) == 1:
            return self.visit(ctx.multiplicativeExpression(0))

        value = self.visit(ctx.multiplicativeExpression(0))
        left = Variable.create_and_assign("left", type(value), value)

        for i, expression in enumerate(ctx.multiplicativeExpression()[1:]):
            next_value = self.visit(expression)
            right = Variable.create_and_assign("right", type(next_value), next_value)

            if ctx.PLUS():
                result = BinaryOperationHandler.addition_handler(left, right)
                left.set_type(type(result))
                left.on_assign(result)
            elif ctx.MINUS():
                result = BinaryOperationHandler.numeric_only_handler(left, right, NumericOnlyOperation.SUBTRACTION)
                left.set_type(type(result))
                left.on_assign(result)

        return left.value

    def visitRelationalExpression(self, ctx: MiniLanguageParser.RelationalExpressionContext):
        if len(ctx.additiveExpression()) == 1:
            return self.visit(ctx.additiveExpression(0))

        left_value = self.visit(ctx.additiveExpression(0))
        left = Variable.create_and_assign("left", type(left_value), left_value)

        right_value = self.visit(ctx.additiveExpression(1))
        right = Variable.create_and_assign("right", type(right_value), right_value)

        relation_ctx = ctx.relation()

        relation_function_map = {
            relation_ctx.LT(): NumericOnlyOperation.LESS_THAN,
            relation_ctx.LE(): NumericOnlyOperation.LESS_THAN_OR_EQUAL,
            relation_ctx.GT(): NumericOnlyOperation.GREATER_THAN,
            relation_ctx.GE(): NumericOnlyOperation.GREATER_THAN_OR_EQUAL,
        }

        for relation, function in relation_function_map.items():
            if relation:
                return BinaryOperationHandler.numeric_only_handler(left, right, function)

    def visitEqualityExpression(self, ctx: MiniLanguageParser.EqualityExpressionContext):
        if len(ctx.relationalExpression()) == 1:
            return self.visit(ctx.relationalExpression(0))

        left_value = self.visit(ctx.relationalExpression(0))
        left = Variable.create_and_assign("left", type(left_value), left_value)

        right_value = self.visit(ctx.relationalExpression(1))
        right = Variable.create_and_assign("right", type(right_value), right_value)

        if ctx.equalityRelation().EQ():
            return BinaryOperationHandler.equality_handler(left, right)
        elif ctx.equalityRelation().NE():
            return BinaryOperationHandler.inequality_handler(left, right)

        raise Exception("Invalid operator")

    def visitLogicalAndExpression(self, ctx: MiniLanguageParser.LogicalAndExpressionContext):
        if len(ctx.equalityExpression()) == 1:
            return self.visit(ctx.equalityExpression(0))

        left_value = self.visit(ctx.equalityExpression(0))
        left = Variable.create_and_assign("left", type(left_value), left_value)

        right_value = self.visit(ctx.equalityExpression(1))
        right = Variable.create_and_assign("right", type(right_value), right_value)

        return BinaryOperationHandler.logical_and_handler(left, right)

    def visitLogicalOrExpression(self, ctx: MiniLanguageParser.LogicalOrExpressionContext):
        if len(ctx.logicalAndExpression()) == 1:
            return self.visit(ctx.logicalAndExpression(0))

        left_value = self.visit(ctx.logicalAndExpression(0))
        left = Variable.create_and_assign("left", type(left_value), left_value)

        right_value = self.visit(ctx.logicalAndExpression(1))
        right = Variable.create_and_assign("right", type(right_value), right_value)

        return BinaryOperationHandler.logical_or_handler(left, right)
