# Generated from C:/Users/asiaw/Desktop/PG/Genetic-Programming/src/main/antlr4/MiniLanguageParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniLanguageParser import MiniLanguageParser
else:
    from MiniLanguageParser import MiniLanguageParser

# This class defines a complete listener for a parse tree produced by MiniLanguageParser.
class MiniLanguageParserListener(ParseTreeListener):

    # Enter a parse tree produced by MiniLanguageParser#program.
    def enterProgram(self, ctx:MiniLanguageParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#program.
    def exitProgram(self, ctx:MiniLanguageParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#block.
    def enterBlock(self, ctx:MiniLanguageParser.BlockContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#block.
    def exitBlock(self, ctx:MiniLanguageParser.BlockContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#statement.
    def enterStatement(self, ctx:MiniLanguageParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#statement.
    def exitStatement(self, ctx:MiniLanguageParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#declStatement.
    def enterDeclStatement(self, ctx:MiniLanguageParser.DeclStatementContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#declStatement.
    def exitDeclStatement(self, ctx:MiniLanguageParser.DeclStatementContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#declWithOptionalAssignment.
    def enterDeclWithOptionalAssignment(self, ctx:MiniLanguageParser.DeclWithOptionalAssignmentContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#declWithOptionalAssignment.
    def exitDeclWithOptionalAssignment(self, ctx:MiniLanguageParser.DeclWithOptionalAssignmentContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:MiniLanguageParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:MiniLanguageParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#ifStatement.
    def enterIfStatement(self, ctx:MiniLanguageParser.IfStatementContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#ifStatement.
    def exitIfStatement(self, ctx:MiniLanguageParser.IfStatementContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#loopStatement.
    def enterLoopStatement(self, ctx:MiniLanguageParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#loopStatement.
    def exitLoopStatement(self, ctx:MiniLanguageParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#read.
    def enterRead(self, ctx:MiniLanguageParser.ReadContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#read.
    def exitRead(self, ctx:MiniLanguageParser.ReadContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#write.
    def enterWrite(self, ctx:MiniLanguageParser.WriteContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#write.
    def exitWrite(self, ctx:MiniLanguageParser.WriteContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:MiniLanguageParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:MiniLanguageParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#unaryExpression.
    def enterUnaryExpression(self, ctx:MiniLanguageParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#unaryExpression.
    def exitUnaryExpression(self, ctx:MiniLanguageParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:MiniLanguageParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:MiniLanguageParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:MiniLanguageParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:MiniLanguageParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#relationalExpression.
    def enterRelationalExpression(self, ctx:MiniLanguageParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#relationalExpression.
    def exitRelationalExpression(self, ctx:MiniLanguageParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#equalityExpression.
    def enterEqualityExpression(self, ctx:MiniLanguageParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#equalityExpression.
    def exitEqualityExpression(self, ctx:MiniLanguageParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:MiniLanguageParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:MiniLanguageParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:MiniLanguageParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:MiniLanguageParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#expression.
    def enterExpression(self, ctx:MiniLanguageParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#expression.
    def exitExpression(self, ctx:MiniLanguageParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#relation.
    def enterRelation(self, ctx:MiniLanguageParser.RelationContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#relation.
    def exitRelation(self, ctx:MiniLanguageParser.RelationContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#equalityRelation.
    def enterEqualityRelation(self, ctx:MiniLanguageParser.EqualityRelationContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#equalityRelation.
    def exitEqualityRelation(self, ctx:MiniLanguageParser.EqualityRelationContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#unaryOperator.
    def enterUnaryOperator(self, ctx:MiniLanguageParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#unaryOperator.
    def exitUnaryOperator(self, ctx:MiniLanguageParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#literal.
    def enterLiteral(self, ctx:MiniLanguageParser.LiteralContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#literal.
    def exitLiteral(self, ctx:MiniLanguageParser.LiteralContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#identifier.
    def enterIdentifier(self, ctx:MiniLanguageParser.IdentifierContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#identifier.
    def exitIdentifier(self, ctx:MiniLanguageParser.IdentifierContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:MiniLanguageParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:MiniLanguageParser.TypeSpecifierContext):
        pass



del MiniLanguageParser