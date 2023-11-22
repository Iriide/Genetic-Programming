from gen.MiniLanguageParserVisitor import MiniLanguageParserVisitor
from gen.MiniLanguageParser import MiniLanguageParser
from types import SimpleType
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

    def visitStatement(self, ctx: MiniLanguageParser.StatementContext):
        self.visitChildren(ctx)

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

    def visitRead(self, ctx: MiniLanguageParser.ReadContext):
        identifier = ctx.identifier().getText()
        value = self.in_file.readline()
        self.variable_memory.assign_variable(identifier, value)

    def visitWrite(self, ctx: MiniLanguageParser.WriteContext):
        value = self.visit(ctx.expression())
        self.out_file.write(str(value))

    def visitExpression(self, ctx: MiniLanguageParser.ExpressionContext):
        return 2137 # Placeholder

