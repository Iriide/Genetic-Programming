# Generated from C:/Users/hikar/Desktop/New programming/Genetic/Grammar/Genetic-Programming/src/main/antlr4\MiniLanguageParser.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniLanguageParser import MiniLanguageParser
else:
    from MiniLanguageParser import MiniLanguageParser

# This class defines a complete generic visitor for a parse tree produced by MiniLanguageParser.

class MiniLanguageParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniLanguageParser#program.
    def visitProgram(self, ctx:MiniLanguageParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLanguageParser#block.
    def visitBlock(self, ctx:MiniLanguageParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLanguageParser#statement.
    def visitStatement(self, ctx:MiniLanguageParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLanguageParser#declStatement.
    def visitDeclStatement(self, ctx:MiniLanguageParser.DeclStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLanguageParser#declWithOptionalAssignment.
    def visitDeclWithOptionalAssignment(self, ctx:MiniLanguageParser.DeclWithOptionalAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLanguageParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:MiniLanguageParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLanguageParser#ifStatement.
    def visitIfStatement(self, ctx:MiniLanguageParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLanguageParser#loopStatement.
    def visitLoopStatement(self, ctx:MiniLanguageParser.LoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLanguageParser#read.
    def visitRead(self, ctx:MiniLanguageParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLanguageParser#write.
    def visitWrite(self, ctx:MiniLanguageParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLanguageParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:MiniLanguageParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLanguageParser#unaryExpression.
    def visitUnaryExpression(self, ctx:MiniLanguageParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLanguageParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:MiniLanguageParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLanguageParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:MiniLanguageParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLanguageParser#relationalExpression.
    def visitRelationalExpression(self, ctx:MiniLanguageParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLanguageParser#equalityExpression.
    def visitEqualityExpression(self, ctx:MiniLanguageParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLanguageParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:MiniLanguageParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLanguageParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:MiniLanguageParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLanguageParser#expression.
    def visitExpression(self, ctx:MiniLanguageParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLanguageParser#relation.
    def visitRelation(self, ctx:MiniLanguageParser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLanguageParser#equalityRelation.
    def visitEqualityRelation(self, ctx:MiniLanguageParser.EqualityRelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLanguageParser#unaryOperator.
    def visitUnaryOperator(self, ctx:MiniLanguageParser.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLanguageParser#literal.
    def visitLiteral(self, ctx:MiniLanguageParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLanguageParser#identifier.
    def visitIdentifier(self, ctx:MiniLanguageParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLanguageParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:MiniLanguageParser.TypeSpecifierContext):
        return self.visitChildren(ctx)



del MiniLanguageParser