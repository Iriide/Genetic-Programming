from visitor import MiniLanguageParser, InterpreterVisitor
from gen.MiniLanguageLexer import MiniLanguageLexer
from antlr4 import FileStream, CommonTokenStream


def main():
    in_file = FileStream('mini_lang/code.test')
    lexer = MiniLanguageLexer(in_file)
    stream = CommonTokenStream(lexer)
    parser = MiniLanguageParser(stream)
    tree = parser.program()

    visitor = InterpreterVisitor('mini_lang/in.in', 'mini_lang/out.out')
    visitor.visit(tree)


if __name__ == '__main__':
    main()
