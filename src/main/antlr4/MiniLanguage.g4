grammar MiniLanguage;

// Parser rules
program     : block EOF ;

block       : '{' statementList '}' ;

statementList
            : statement* ;

statement   : assignmentStatement
            | ifStatement
            | loopStatement
            | read
            | write
            ;

assignmentStatement
            : variable '=' expression ';' ;

ifStatement : 'if' '(' condition ')' block ( 'else' block )? ;

loopStatement
            : 'while' '(' condition ')' block ;

read : 'read' '(' variable ')' ';';

write : 'write' '(' expression ')' ';';

expression  : expression ('+' | '-') term
            | term
            ;

term        : term ('*' | '/') factor
            | factor
            ;

factor      : number
            | variable
            | '(' expression ')'
            | unaryOperator factor
            ;

condition   : expression relation expression ;

relation    : '<' | '<=' | '==' | '!=' | '>=' | '>'
            ;

// Lexer rules
unaryOperator
            : '+' | '-' | '!'
            ;

number      : '-'? DIGIT+ ;

variable    : LETTER (LETTER | DIGIT)* ;

LETTER      : [a-zA-Z] ;

DIGIT       : [0-9] ;

// ????
WS          : [ \t\r\n]+ -> skip ;

COMMENT     : '//' .*? '\n' -> skip ;
