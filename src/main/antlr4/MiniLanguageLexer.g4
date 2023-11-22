lexer grammar MiniLanguageLexer;

COMMA: ',';
DOT: '.';
QUOTE: '"';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';

// Operations
PLUS: '+';
MINUS: '-';
TIMES: '*';
DIV: '/';

// Assignment operators
ASSIGN: '=';
SEMI: ';';

// Literals
INTEGER_LITERAL : DEC_DIGIT (DEC_DIGIT | '_')*;
FLOAT_LITERAL   : INTEGER_LITERAL DOT INTEGER_LITERAL;
BOOL_LITERAL    : KW_TRUE | KW_FALSE;
STRING_LITERAL  : QUOTE
    (
        ~["]
        | QUOTE_ESCAPE
        | NEWLINE_ESCAPE
    )* QUOTE
    ;

// Keywords
KW_IF: 'if';
KW_ELSE: 'else';
KW_WHILE: 'while';
KW_READ: 'read';
KW_WRITE: 'write';
KW_TRUE: 'true';
KW_FALSE: 'false';

// Logical operators
AND: '&&';
OR: '||';

// Types
KW_INT: 'int';
KW_BOOL: 'bool';
KW_FLOAT: 'float';
KW_STRING: 'string';

// Relations
EQ: '==';
NE: '!=';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';
NOT: '!';

IDENTIFIER
    : [A-Za-z_]+ [A-Za-z_0-9]*
    ;
WS          : [ \t\r\n]+ -> skip;
DIGIT       : [0-9];
LETTER      : [a-zA-Z];

// Fragments
fragment DEC_DIGIT: [0-9];
fragment QUOTE_ESCAPE: '\\' ['"];
fragment NEWLINE_ESCAPE: '\\' '\n';
