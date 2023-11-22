# Generated from C:/Users/hikar/Desktop/New programming/Genetic/Grammar/Genetic-Programming/src/main/antlr4\MiniLanguageParser.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,41,206,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,5,0,52,8,0,10,0,
        12,0,55,9,0,1,0,1,0,1,1,1,1,5,1,61,8,1,10,1,12,1,64,9,1,1,1,1,1,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,77,8,2,1,3,1,3,1,3,1,3,5,
        3,83,8,3,10,3,12,3,86,9,3,1,3,1,3,1,4,1,4,1,4,3,4,93,8,4,1,5,1,5,
        1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,111,
        8,6,10,6,12,6,114,9,6,1,6,1,6,3,6,118,8,6,1,7,1,7,1,7,3,7,123,8,
        7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,
        10,1,10,1,10,1,10,1,10,1,10,3,10,146,8,10,1,11,1,11,1,11,1,11,3,
        11,152,8,11,1,12,1,12,1,12,5,12,157,8,12,10,12,12,12,160,9,12,1,
        13,1,13,1,13,5,13,165,8,13,10,13,12,13,168,9,13,1,14,1,14,1,14,1,
        14,3,14,174,8,14,1,15,1,15,1,15,1,15,3,15,180,8,15,1,16,1,16,1,16,
        3,16,185,8,16,1,17,1,17,1,17,3,17,190,8,17,1,18,1,18,1,19,1,19,1,
        20,1,20,1,21,1,21,1,22,1,22,1,23,1,23,1,24,1,24,1,24,0,0,25,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        0,7,1,0,10,11,1,0,8,9,1,0,33,36,1,0,31,32,2,0,8,9,37,37,1,0,14,17,
        1,0,27,30,202,0,53,1,0,0,0,2,58,1,0,0,0,4,76,1,0,0,0,6,78,1,0,0,
        0,8,89,1,0,0,0,10,94,1,0,0,0,12,98,1,0,0,0,14,119,1,0,0,0,16,127,
        1,0,0,0,18,133,1,0,0,0,20,145,1,0,0,0,22,151,1,0,0,0,24,153,1,0,
        0,0,26,161,1,0,0,0,28,169,1,0,0,0,30,175,1,0,0,0,32,181,1,0,0,0,
        34,186,1,0,0,0,36,191,1,0,0,0,38,193,1,0,0,0,40,195,1,0,0,0,42,197,
        1,0,0,0,44,199,1,0,0,0,46,201,1,0,0,0,48,203,1,0,0,0,50,52,3,4,2,
        0,51,50,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,56,
        1,0,0,0,55,53,1,0,0,0,56,57,5,0,0,1,57,1,1,0,0,0,58,62,5,6,0,0,59,
        61,3,4,2,0,60,59,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,
        0,63,65,1,0,0,0,64,62,1,0,0,0,65,66,5,7,0,0,66,3,1,0,0,0,67,68,3,
        10,5,0,68,69,5,13,0,0,69,77,1,0,0,0,70,77,3,6,3,0,71,77,3,14,7,0,
        72,77,3,12,6,0,73,77,3,16,8,0,74,77,3,18,9,0,75,77,3,2,1,0,76,67,
        1,0,0,0,76,70,1,0,0,0,76,71,1,0,0,0,76,72,1,0,0,0,76,73,1,0,0,0,
        76,74,1,0,0,0,76,75,1,0,0,0,77,5,1,0,0,0,78,79,3,48,24,0,79,84,3,
        8,4,0,80,81,5,1,0,0,81,83,3,8,4,0,82,80,1,0,0,0,83,86,1,0,0,0,84,
        82,1,0,0,0,84,85,1,0,0,0,85,87,1,0,0,0,86,84,1,0,0,0,87,88,5,13,
        0,0,88,7,1,0,0,0,89,92,3,46,23,0,90,91,5,12,0,0,91,93,3,36,18,0,
        92,90,1,0,0,0,92,93,1,0,0,0,93,9,1,0,0,0,94,95,3,46,23,0,95,96,5,
        12,0,0,96,97,3,36,18,0,97,11,1,0,0,0,98,99,5,18,0,0,99,100,5,4,0,
        0,100,101,3,36,18,0,101,102,5,5,0,0,102,112,3,4,2,0,103,104,5,19,
        0,0,104,105,5,18,0,0,105,106,5,4,0,0,106,107,3,36,18,0,107,108,5,
        5,0,0,108,109,3,4,2,0,109,111,1,0,0,0,110,103,1,0,0,0,111,114,1,
        0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,117,1,0,0,0,114,112,1,
        0,0,0,115,116,5,19,0,0,116,118,3,4,2,0,117,115,1,0,0,0,117,118,1,
        0,0,0,118,13,1,0,0,0,119,120,5,20,0,0,120,122,5,4,0,0,121,123,3,
        36,18,0,122,121,1,0,0,0,122,123,1,0,0,0,123,124,1,0,0,0,124,125,
        5,5,0,0,125,126,3,4,2,0,126,15,1,0,0,0,127,128,5,21,0,0,128,129,
        5,4,0,0,129,130,3,46,23,0,130,131,5,5,0,0,131,132,5,13,0,0,132,17,
        1,0,0,0,133,134,5,22,0,0,134,135,5,4,0,0,135,136,3,36,18,0,136,137,
        5,5,0,0,137,138,5,13,0,0,138,19,1,0,0,0,139,146,3,44,22,0,140,146,
        3,46,23,0,141,142,5,4,0,0,142,143,3,36,18,0,143,144,5,5,0,0,144,
        146,1,0,0,0,145,139,1,0,0,0,145,140,1,0,0,0,145,141,1,0,0,0,146,
        21,1,0,0,0,147,148,3,42,21,0,148,149,3,22,11,0,149,152,1,0,0,0,150,
        152,3,20,10,0,151,147,1,0,0,0,151,150,1,0,0,0,152,23,1,0,0,0,153,
        158,3,22,11,0,154,155,7,0,0,0,155,157,3,22,11,0,156,154,1,0,0,0,
        157,160,1,0,0,0,158,156,1,0,0,0,158,159,1,0,0,0,159,25,1,0,0,0,160,
        158,1,0,0,0,161,166,3,24,12,0,162,163,7,1,0,0,163,165,3,24,12,0,
        164,162,1,0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,0,
        167,27,1,0,0,0,168,166,1,0,0,0,169,173,3,26,13,0,170,171,3,38,19,
        0,171,172,3,26,13,0,172,174,1,0,0,0,173,170,1,0,0,0,173,174,1,0,
        0,0,174,29,1,0,0,0,175,179,3,28,14,0,176,177,3,40,20,0,177,178,3,
        28,14,0,178,180,1,0,0,0,179,176,1,0,0,0,179,180,1,0,0,0,180,31,1,
        0,0,0,181,184,3,30,15,0,182,183,5,25,0,0,183,185,3,30,15,0,184,182,
        1,0,0,0,184,185,1,0,0,0,185,33,1,0,0,0,186,189,3,32,16,0,187,188,
        5,26,0,0,188,190,3,32,16,0,189,187,1,0,0,0,189,190,1,0,0,0,190,35,
        1,0,0,0,191,192,3,34,17,0,192,37,1,0,0,0,193,194,7,2,0,0,194,39,
        1,0,0,0,195,196,7,3,0,0,196,41,1,0,0,0,197,198,7,4,0,0,198,43,1,
        0,0,0,199,200,7,5,0,0,200,45,1,0,0,0,201,202,5,38,0,0,202,47,1,0,
        0,0,203,204,7,6,0,0,204,49,1,0,0,0,16,53,62,76,84,92,112,117,122,
        145,151,158,166,173,179,184,189
    ]

class MiniLanguageParser ( Parser ):

    grammarFileName = "MiniLanguageParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'.'", "'\"'", "'('", "')'", "'{'", 
                     "'}'", "'+'", "'-'", "'*'", "'/'", "'='", "';'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'if'", "'else'", 
                     "'while'", "'read'", "'write'", "'true'", "'false'", 
                     "'&&'", "'||'", "'int'", "'bool'", "'float'", "'string'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'!'" ]

    symbolicNames = [ "<INVALID>", "COMMA", "DOT", "QUOTE", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "PLUS", "MINUS", "TIMES", "DIV", 
                      "ASSIGN", "SEMI", "INTEGER_LITERAL", "FLOAT_LITERAL", 
                      "BOOL_LITERAL", "STRING_LITERAL", "KW_IF", "KW_ELSE", 
                      "KW_WHILE", "KW_READ", "KW_WRITE", "KW_TRUE", "KW_FALSE", 
                      "AND", "OR", "KW_INT", "KW_BOOL", "KW_FLOAT", "KW_STRING", 
                      "EQ", "NE", "LT", "GT", "LE", "GE", "NOT", "IDENTIFIER", 
                      "WS", "DIGIT", "LETTER" ]

    RULE_program = 0
    RULE_block = 1
    RULE_statement = 2
    RULE_declStatement = 3
    RULE_declWithOptionalAssignment = 4
    RULE_assignmentStatement = 5
    RULE_ifStatement = 6
    RULE_loopStatement = 7
    RULE_read = 8
    RULE_write = 9
    RULE_primaryExpression = 10
    RULE_unaryExpression = 11
    RULE_multiplicativeExpression = 12
    RULE_additiveExpression = 13
    RULE_relationalExpression = 14
    RULE_equalityExpression = 15
    RULE_logicalAndExpression = 16
    RULE_logicalOrExpression = 17
    RULE_expression = 18
    RULE_relation = 19
    RULE_equalityRelation = 20
    RULE_unaryOperator = 21
    RULE_literal = 22
    RULE_identifier = 23
    RULE_typeSpecifier = 24

    ruleNames =  [ "program", "block", "statement", "declStatement", "declWithOptionalAssignment", 
                   "assignmentStatement", "ifStatement", "loopStatement", 
                   "read", "write", "primaryExpression", "unaryExpression", 
                   "multiplicativeExpression", "additiveExpression", "relationalExpression", 
                   "equalityExpression", "logicalAndExpression", "logicalOrExpression", 
                   "expression", "relation", "equalityRelation", "unaryOperator", 
                   "literal", "identifier", "typeSpecifier" ]

    EOF = Token.EOF
    COMMA=1
    DOT=2
    QUOTE=3
    LPAREN=4
    RPAREN=5
    LBRACE=6
    RBRACE=7
    PLUS=8
    MINUS=9
    TIMES=10
    DIV=11
    ASSIGN=12
    SEMI=13
    INTEGER_LITERAL=14
    FLOAT_LITERAL=15
    BOOL_LITERAL=16
    STRING_LITERAL=17
    KW_IF=18
    KW_ELSE=19
    KW_WHILE=20
    KW_READ=21
    KW_WRITE=22
    KW_TRUE=23
    KW_FALSE=24
    AND=25
    OR=26
    KW_INT=27
    KW_BOOL=28
    KW_FLOAT=29
    KW_STRING=30
    EQ=31
    NE=32
    LT=33
    GT=34
    LE=35
    GE=36
    NOT=37
    IDENTIFIER=38
    WS=39
    DIGIT=40
    LETTER=41

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniLanguageParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniLanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniLanguageParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniLanguageParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 276898775104) != 0):
                self.state = 50
                self.statement()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 56
            self.match(MiniLanguageParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniLanguageParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniLanguageParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniLanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniLanguageParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniLanguageParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(MiniLanguageParser.LBRACE)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 276898775104) != 0):
                self.state = 59
                self.statement()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
            self.match(MiniLanguageParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentStatement(self):
            return self.getTypedRuleContext(MiniLanguageParser.AssignmentStatementContext,0)


        def SEMI(self):
            return self.getToken(MiniLanguageParser.SEMI, 0)

        def declStatement(self):
            return self.getTypedRuleContext(MiniLanguageParser.DeclStatementContext,0)


        def loopStatement(self):
            return self.getTypedRuleContext(MiniLanguageParser.LoopStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MiniLanguageParser.IfStatementContext,0)


        def read(self):
            return self.getTypedRuleContext(MiniLanguageParser.ReadContext,0)


        def write(self):
            return self.getTypedRuleContext(MiniLanguageParser.WriteContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniLanguageParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniLanguageParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniLanguageParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.assignmentStatement()
                self.state = 68
                self.match(MiniLanguageParser.SEMI)
                pass
            elif token in [27, 28, 29, 30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.declStatement()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 71
                self.loopStatement()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.ifStatement()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 5)
                self.state = 73
                self.read()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 6)
                self.state = 74
                self.write()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 7)
                self.state = 75
                self.block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(MiniLanguageParser.TypeSpecifierContext,0)


        def declWithOptionalAssignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLanguageParser.DeclWithOptionalAssignmentContext)
            else:
                return self.getTypedRuleContext(MiniLanguageParser.DeclWithOptionalAssignmentContext,i)


        def SEMI(self):
            return self.getToken(MiniLanguageParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLanguageParser.COMMA)
            else:
                return self.getToken(MiniLanguageParser.COMMA, i)

        def getRuleIndex(self):
            return MiniLanguageParser.RULE_declStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclStatement" ):
                listener.enterDeclStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclStatement" ):
                listener.exitDeclStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclStatement" ):
                return visitor.visitDeclStatement(self)
            else:
                return visitor.visitChildren(self)




    def declStatement(self):

        localctx = MiniLanguageParser.DeclStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.typeSpecifier()
            self.state = 79
            self.declWithOptionalAssignment()
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 80
                self.match(MiniLanguageParser.COMMA)
                self.state = 81
                self.declWithOptionalAssignment()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 87
            self.match(MiniLanguageParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclWithOptionalAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(MiniLanguageParser.IdentifierContext,0)


        def ASSIGN(self):
            return self.getToken(MiniLanguageParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniLanguageParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniLanguageParser.RULE_declWithOptionalAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclWithOptionalAssignment" ):
                listener.enterDeclWithOptionalAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclWithOptionalAssignment" ):
                listener.exitDeclWithOptionalAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclWithOptionalAssignment" ):
                return visitor.visitDeclWithOptionalAssignment(self)
            else:
                return visitor.visitChildren(self)




    def declWithOptionalAssignment(self):

        localctx = MiniLanguageParser.DeclWithOptionalAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declWithOptionalAssignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.identifier()
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 90
                self.match(MiniLanguageParser.ASSIGN)
                self.state = 91
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(MiniLanguageParser.IdentifierContext,0)


        def ASSIGN(self):
            return self.getToken(MiniLanguageParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniLanguageParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniLanguageParser.RULE_assignmentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = MiniLanguageParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.identifier()
            self.state = 95
            self.match(MiniLanguageParser.ASSIGN)
            self.state = 96
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_IF(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLanguageParser.KW_IF)
            else:
                return self.getToken(MiniLanguageParser.KW_IF, i)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLanguageParser.LPAREN)
            else:
                return self.getToken(MiniLanguageParser.LPAREN, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniLanguageParser.ExpressionContext,i)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLanguageParser.RPAREN)
            else:
                return self.getToken(MiniLanguageParser.RPAREN, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniLanguageParser.StatementContext,i)


        def KW_ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLanguageParser.KW_ELSE)
            else:
                return self.getToken(MiniLanguageParser.KW_ELSE, i)

        def getRuleIndex(self):
            return MiniLanguageParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = MiniLanguageParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(MiniLanguageParser.KW_IF)
            self.state = 99
            self.match(MiniLanguageParser.LPAREN)
            self.state = 100
            self.expression()
            self.state = 101
            self.match(MiniLanguageParser.RPAREN)
            self.state = 102
            self.statement()
            self.state = 112
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 103
                    self.match(MiniLanguageParser.KW_ELSE)
                    self.state = 104
                    self.match(MiniLanguageParser.KW_IF)
                    self.state = 105
                    self.match(MiniLanguageParser.LPAREN)
                    self.state = 106
                    self.expression()
                    self.state = 107
                    self.match(MiniLanguageParser.RPAREN)
                    self.state = 108
                    self.statement() 
                self.state = 114
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 115
                self.match(MiniLanguageParser.KW_ELSE)
                self.state = 116
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_WHILE(self):
            return self.getToken(MiniLanguageParser.KW_WHILE, 0)

        def LPAREN(self):
            return self.getToken(MiniLanguageParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniLanguageParser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(MiniLanguageParser.StatementContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniLanguageParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniLanguageParser.RULE_loopStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatement" ):
                listener.enterLoopStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatement" ):
                listener.exitLoopStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopStatement" ):
                return visitor.visitLoopStatement(self)
            else:
                return visitor.visitChildren(self)




    def loopStatement(self):

        localctx = MiniLanguageParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_loopStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(MiniLanguageParser.KW_WHILE)
            self.state = 120
            self.match(MiniLanguageParser.LPAREN)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 412317106960) != 0):
                self.state = 121
                self.expression()


            self.state = 124
            self.match(MiniLanguageParser.RPAREN)
            self.state = 125
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_READ(self):
            return self.getToken(MiniLanguageParser.KW_READ, 0)

        def LPAREN(self):
            return self.getToken(MiniLanguageParser.LPAREN, 0)

        def identifier(self):
            return self.getTypedRuleContext(MiniLanguageParser.IdentifierContext,0)


        def RPAREN(self):
            return self.getToken(MiniLanguageParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(MiniLanguageParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniLanguageParser.RULE_read

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead" ):
                return visitor.visitRead(self)
            else:
                return visitor.visitChildren(self)




    def read(self):

        localctx = MiniLanguageParser.ReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_read)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(MiniLanguageParser.KW_READ)
            self.state = 128
            self.match(MiniLanguageParser.LPAREN)
            self.state = 129
            self.identifier()
            self.state = 130
            self.match(MiniLanguageParser.RPAREN)
            self.state = 131
            self.match(MiniLanguageParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_WRITE(self):
            return self.getToken(MiniLanguageParser.KW_WRITE, 0)

        def LPAREN(self):
            return self.getToken(MiniLanguageParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniLanguageParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniLanguageParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(MiniLanguageParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniLanguageParser.RULE_write

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite" ):
                listener.enterWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite" ):
                listener.exitWrite(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)




    def write(self):

        localctx = MiniLanguageParser.WriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_write)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(MiniLanguageParser.KW_WRITE)
            self.state = 134
            self.match(MiniLanguageParser.LPAREN)
            self.state = 135
            self.expression()
            self.state = 136
            self.match(MiniLanguageParser.RPAREN)
            self.state = 137
            self.match(MiniLanguageParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniLanguageParser.LiteralContext,0)


        def identifier(self):
            return self.getTypedRuleContext(MiniLanguageParser.IdentifierContext,0)


        def LPAREN(self):
            return self.getToken(MiniLanguageParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniLanguageParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniLanguageParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniLanguageParser.RULE_primaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpression" ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpression" ):
                listener.exitPrimaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpression(self):

        localctx = MiniLanguageParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_primaryExpression)
        try:
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14, 15, 16, 17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.literal()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.identifier()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 141
                self.match(MiniLanguageParser.LPAREN)
                self.state = 142
                self.expression()
                self.state = 143
                self.match(MiniLanguageParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryOperator(self):
            return self.getTypedRuleContext(MiniLanguageParser.UnaryOperatorContext,0)


        def unaryExpression(self):
            return self.getTypedRuleContext(MiniLanguageParser.UnaryExpressionContext,0)


        def primaryExpression(self):
            return self.getTypedRuleContext(MiniLanguageParser.PrimaryExpressionContext,0)


        def getRuleIndex(self):
            return MiniLanguageParser.RULE_unaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpression" ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpression" ):
                listener.exitUnaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpression" ):
                return visitor.visitUnaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpression(self):

        localctx = MiniLanguageParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_unaryExpression)
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.unaryOperator()
                self.state = 148
                self.unaryExpression()
                pass
            elif token in [4, 14, 15, 16, 17, 38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.primaryExpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLanguageParser.UnaryExpressionContext)
            else:
                return self.getTypedRuleContext(MiniLanguageParser.UnaryExpressionContext,i)


        def TIMES(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLanguageParser.TIMES)
            else:
                return self.getToken(MiniLanguageParser.TIMES, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLanguageParser.DIV)
            else:
                return self.getToken(MiniLanguageParser.DIV, i)

        def getRuleIndex(self):
            return MiniLanguageParser.RULE_multiplicativeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpression(self):

        localctx = MiniLanguageParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.unaryExpression()
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10 or _la==11:
                self.state = 154
                _la = self._input.LA(1)
                if not(_la==10 or _la==11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 155
                self.unaryExpression()
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLanguageParser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(MiniLanguageParser.MultiplicativeExpressionContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLanguageParser.PLUS)
            else:
                return self.getToken(MiniLanguageParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLanguageParser.MINUS)
            else:
                return self.getToken(MiniLanguageParser.MINUS, i)

        def getRuleIndex(self):
            return MiniLanguageParser.RULE_additiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpression(self):

        localctx = MiniLanguageParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.multiplicativeExpression()
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8 or _la==9:
                self.state = 162
                _la = self._input.LA(1)
                if not(_la==8 or _la==9):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 163
                self.multiplicativeExpression()
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLanguageParser.AdditiveExpressionContext)
            else:
                return self.getTypedRuleContext(MiniLanguageParser.AdditiveExpressionContext,i)


        def relation(self):
            return self.getTypedRuleContext(MiniLanguageParser.RelationContext,0)


        def getRuleIndex(self):
            return MiniLanguageParser.RULE_relationalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpression" ):
                listener.enterRelationalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpression" ):
                listener.exitRelationalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpression" ):
                return visitor.visitRelationalExpression(self)
            else:
                return visitor.visitChildren(self)




    def relationalExpression(self):

        localctx = MiniLanguageParser.RelationalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_relationalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.additiveExpression()
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 128849018880) != 0):
                self.state = 170
                self.relation()
                self.state = 171
                self.additiveExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLanguageParser.RelationalExpressionContext)
            else:
                return self.getTypedRuleContext(MiniLanguageParser.RelationalExpressionContext,i)


        def equalityRelation(self):
            return self.getTypedRuleContext(MiniLanguageParser.EqualityRelationContext,0)


        def getRuleIndex(self):
            return MiniLanguageParser.RULE_equalityExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpression" ):
                listener.enterEqualityExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpression" ):
                listener.exitEqualityExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpression" ):
                return visitor.visitEqualityExpression(self)
            else:
                return visitor.visitChildren(self)




    def equalityExpression(self):

        localctx = MiniLanguageParser.EqualityExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_equalityExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.relationalExpression()
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31 or _la==32:
                self.state = 176
                self.equalityRelation()
                self.state = 177
                self.relationalExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLanguageParser.EqualityExpressionContext)
            else:
                return self.getTypedRuleContext(MiniLanguageParser.EqualityExpressionContext,i)


        def AND(self):
            return self.getToken(MiniLanguageParser.AND, 0)

        def getRuleIndex(self):
            return MiniLanguageParser.RULE_logicalAndExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAndExpression" ):
                listener.enterLogicalAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAndExpression" ):
                listener.exitLogicalAndExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAndExpression" ):
                return visitor.visitLogicalAndExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalAndExpression(self):

        localctx = MiniLanguageParser.LogicalAndExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_logicalAndExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.equalityExpression()
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 182
                self.match(MiniLanguageParser.AND)
                self.state = 183
                self.equalityExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAndExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLanguageParser.LogicalAndExpressionContext)
            else:
                return self.getTypedRuleContext(MiniLanguageParser.LogicalAndExpressionContext,i)


        def OR(self):
            return self.getToken(MiniLanguageParser.OR, 0)

        def getRuleIndex(self):
            return MiniLanguageParser.RULE_logicalOrExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOrExpression" ):
                listener.enterLogicalOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOrExpression" ):
                listener.exitLogicalOrExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOrExpression" ):
                return visitor.visitLogicalOrExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalOrExpression(self):

        localctx = MiniLanguageParser.LogicalOrExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_logicalOrExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.logicalAndExpression()
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 187
                self.match(MiniLanguageParser.OR)
                self.state = 188
                self.logicalAndExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalOrExpression(self):
            return self.getTypedRuleContext(MiniLanguageParser.LogicalOrExpressionContext,0)


        def getRuleIndex(self):
            return MiniLanguageParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MiniLanguageParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.logicalOrExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(MiniLanguageParser.LT, 0)

        def LE(self):
            return self.getToken(MiniLanguageParser.LE, 0)

        def GT(self):
            return self.getToken(MiniLanguageParser.GT, 0)

        def GE(self):
            return self.getToken(MiniLanguageParser.GE, 0)

        def getRuleIndex(self):
            return MiniLanguageParser.RULE_relation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelation" ):
                listener.enterRelation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelation" ):
                listener.exitRelation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation" ):
                return visitor.visitRelation(self)
            else:
                return visitor.visitChildren(self)




    def relation(self):

        localctx = MiniLanguageParser.RelationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_relation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 128849018880) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityRelationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(MiniLanguageParser.EQ, 0)

        def NE(self):
            return self.getToken(MiniLanguageParser.NE, 0)

        def getRuleIndex(self):
            return MiniLanguageParser.RULE_equalityRelation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityRelation" ):
                listener.enterEqualityRelation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityRelation" ):
                listener.exitEqualityRelation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityRelation" ):
                return visitor.visitEqualityRelation(self)
            else:
                return visitor.visitChildren(self)




    def equalityRelation(self):

        localctx = MiniLanguageParser.EqualityRelationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_equalityRelation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            _la = self._input.LA(1)
            if not(_la==31 or _la==32):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(MiniLanguageParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MiniLanguageParser.MINUS, 0)

        def NOT(self):
            return self.getToken(MiniLanguageParser.NOT, 0)

        def getRuleIndex(self):
            return MiniLanguageParser.RULE_unaryOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryOperator" ):
                listener.enterUnaryOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryOperator" ):
                listener.exitUnaryOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryOperator" ):
                return visitor.visitUnaryOperator(self)
            else:
                return visitor.visitChildren(self)




    def unaryOperator(self):

        localctx = MiniLanguageParser.UnaryOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_unaryOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 137438954240) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL_LITERAL(self):
            return self.getToken(MiniLanguageParser.BOOL_LITERAL, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(MiniLanguageParser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(MiniLanguageParser.FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(MiniLanguageParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return MiniLanguageParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniLanguageParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniLanguageParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniLanguageParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = MiniLanguageParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(MiniLanguageParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_INT(self):
            return self.getToken(MiniLanguageParser.KW_INT, 0)

        def KW_BOOL(self):
            return self.getToken(MiniLanguageParser.KW_BOOL, 0)

        def KW_FLOAT(self):
            return self.getToken(MiniLanguageParser.KW_FLOAT, 0)

        def KW_STRING(self):
            return self.getToken(MiniLanguageParser.KW_STRING, 0)

        def getRuleIndex(self):
            return MiniLanguageParser.RULE_typeSpecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSpecifier" ):
                listener.enterTypeSpecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSpecifier" ):
                listener.exitTypeSpecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeSpecifier" ):
                return visitor.visitTypeSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def typeSpecifier(self):

        localctx = MiniLanguageParser.TypeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_typeSpecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2013265920) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





