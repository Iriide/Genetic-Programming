parser grammar MiniLanguageParser;
options { tokenVocab=MiniLanguageLexer; }

program     : statement* EOF;

block       : LBRACE statement* RBRACE;

statement   : assignmentStatement SEMI
            | declStatement
            | loopStatement
            | ifStatement
            | read
            | write
            | block
            ;

declStatement
            : typeSpecifier declWithOptionalAssignment (declWithOptionalAssignment)* SEMI;

declWithOptionalAssignment
            : identifier (ASSIGN expression)?;

assignmentStatement
            : identifier ASSIGN expression;

ifStatement : KW_IF LPAREN expression RPAREN statement (KW_ELSE KW_IF LPAREN expression RPAREN statement)* (KW_ELSE statement)?;

loopStatement
            : KW_WHILE LPAREN expression? RPAREN statement;

read        : KW_READ LPAREN identifier RPAREN SEMI;

write       : KW_WRITE LPAREN expression RPAREN SEMI;

primaryExpression
            : literal
            | identifier
            | LPAREN expression RPAREN
            ;

unaryExpression
            : unaryOperator unaryExpression
            | primaryExpression;

multiplicativeExpression
            : unaryExpression ((TIMES | DIV) unaryExpression)*
            ;

additiveExpression
            : multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*
            ;

relationalExpression
            : additiveExpression (relation additiveExpression)*
            ;

equalityExpression
            : relationalExpression (equalityRelation relationalExpression)*
            ;

logicalAndExpression
            : equalityExpression (AND equalityExpression)*
            ;

logicalOrExpression
            : logicalAndExpression (OR logicalAndExpression)*
            ;

expression  : logicalOrExpression;

relation    : (LT | LE | GT | GE);

equalityRelation
            : (EQ | NE);

unaryOperator
            : PLUS | MINUS | NOT;

literal     : BOOL_LITERAL
            | INTEGER_LITERAL
            | FLOAT_LITERAL
            | STRING_LITERAL
            ;

identifier  : IDENTIFIER;

typeSpecifier
            : KW_INT
            | KW_BOOL
            | KW_FLOAT
            | KW_STRING
            ;