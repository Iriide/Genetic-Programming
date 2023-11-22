import logging

from visitor_ import MiniLanguageParser, InterpreterVisitor
from gen.MiniLanguageLexer import MiniLanguageLexer

from antlr4 import *

in_file = FileStream('code.test')
lexer = MiniLanguageLexer(in_file)
stream = CommonTokenStream(lexer)
parser = MiniLanguageParser(stream)
tree = parser.program()

visitor = InterpreterVisitor('in.in', 'out.out')
visitor.visit(tree)

