from gen.MiniLanguageParserVisitor import MiniLanguageParserVisitor
from gen.MiniLanguageParser import MiniLanguageParser
from types_ import SimpleType
from typing import TextIO

from variables.memory import VariableMemory


class MiniLangParser(MiniLanguageParserVisitor):

    in_file: TextIO
    out_file: TextIO
    variable_memory: VariableMemory

    def __init__(self, in_path: str, out_path: str):
        super().__init__()

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
        identifier = ctx.identifier().getText()
        value = self.in_file.readline()
        self.variable_memory.assign_variable(identifier, value)

    def visitWrite(self, ctx: MiniLanguageParser.WriteContext):
        value = self.visit(ctx.expression())
        self.out_file.write(str(value))

    def visitExpression(self, ctx: MiniLanguageParser.ExpressionContext):
        return self.visit(ctx.children[0])

    def visitPrimaryExpression(self, ctx: MiniLanguageParser.PrimaryExpressionContext):
        return self.visit(ctx.children[0])

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
            if value.get_type() != SimpleType.INT or value.get_type() != SimpleType.FLOAT:
                raise Exception("Invalid operator")
            if ctx.TIMES()[expression - 1]:
                value *= self.visit(ctx.unaryExpression()[expression])
            elif ctx.DIV()[expression - 1] and self.visit(ctx.unaryExpression()[expression]) != 0:
                value /= self.visit(ctx.unaryExpression()[expression])

        return value

    def visitAdditiveExpression(self, ctx: MiniLanguageParser.AdditiveExpressionContext):
        value = self.visit(ctx.multiplicativeExpression()[0])

        for expression in range(1, len(ctx.multiplicativeExpression())):
            if value.get_type() == SimpleType.BOOL:
                raise Exception("Invalid operator")
            if ctx.PLUS()[expression - 1]:
                value += self.visit(ctx.multiplicativeExpression()[expression])
            elif ctx.MINUS()[expression - 1]:
                value -= self.visit(ctx.multiplicativeExpression()[expression])

        return value

    def visitRelationalExpression(self, ctx: MiniLanguageParser.RelationalExpressionContext):
        if len(ctx.additiveExpression()) == 1:
            return self.visit(ctx.additiveExpression(0))

        left = self.visit(ctx.additiveExpression(0))
        right = self.visit(ctx.additiveExpression(1))

        if ctx.relation().LT():
            return left < right
        elif ctx.relation().LE():
            return left <= right
        elif ctx.relation().GT():
            return left > right
        elif ctx.relation().GE():
            return left >= right

        raise Exception("Invalid operator")

    def visitEqualityExpression(self, ctx: MiniLanguageParser.EqualityExpressionContext):
        if len(ctx.relationalExpression()) == 1:
            return self.visit(ctx.relationalExpression(0))

        left = self.visit(ctx.relationalExpression(0))
        right = self.visit(ctx.relationalExpression(1))

        if ctx.equalityRelation().EQ():
            return left == right
        elif ctx.equalityRelation().NE():
            return left != right

        raise Exception("Invalid operator")

    def visitLogicalAndExpression(self, ctx: MiniLanguageParser.LogicalAndExpressionContext):
        if len(ctx.equalityExpression()) == 1:
            return self.visit(ctx.equalityExpression(0))

        left = self.visit(ctx.equalityExpression(0))
        right = self.visit(ctx.equalityExpression(1))

        if left.get_type() != SimpleType.BOOL or right.get_type() != SimpleType.BOOL:
            raise Exception("Invalid operator")

        return left and right

    def visitLogicalOrExpression(self, ctx: MiniLanguageParser.LogicalOrExpressionContext):
        if len(ctx.logicalAndExpression()) == 1:
            return self.visit(ctx.logicalAndExpression(0))

        left = self.visit(ctx.logicalAndExpression(0))
        right = self.visit(ctx.logicalAndExpression(1))

        if left.get_type() != SimpleType.BOOL or right.get_type() != SimpleType.BOOL:
            raise Exception("Invalid operator")
        return left or right

    def visitRelation(self, ctx: MiniLanguageParser.RelationContext):
        return self.visit(ctx.children[0])

    def visitEqualityRelation(self, ctx: MiniLanguageParser.EqualityRelationContext):
        return self.visit(ctx.children[0])

    def visitUnaryOperator(self, ctx: MiniLanguageParser.UnaryOperatorContext):
        return self.visit(ctx.children[0])

    def visitLiteral(self, ctx: MiniLanguageParser.LiteralContext):
        return self.visit(ctx.children[0])

    def visitIdentifier(self, ctx: MiniLanguageParser.IdentifierContext):
        return self.visit(ctx.children[0])

    def visitTypeSpecifier(self, ctx: MiniLanguageParser.TypeSpecifierContext):
        return self.visit(ctx.children[0])


