
//CFilter.g4
//按照条件过滤数据规则,返回结果为bool

grammar CFilter;


cfilter
    : expressionStatement? EOF
    ;

expressionStatement
    : expression ';'?
    ;

expression
    : sign expression       # signedExpression
    | notOp expression                            # notExpression
    | '(' expression ')'    # parentExpression
    | expression firstPrecedenceMathOperator expression     # fpMathOperatorExpression
    | expression secondPrecedenceMathOperator expression    # spMathOperatorExpression
    | expression compareOperator expression                 # cOperatorExpression
    | expression logicalXor expression                      # logicXorExpression
    | expression logicalAnd expression                      # logicAndExpression
    | expression logicalOr expression                       # logicOrExpression
    | funcCall '('functionArgs?')'                          # functionCallExpression
    | decimalLiteral        # literalExpression
    | stringLiteral         # strLiteralExpression
    | identifier            # identifierExpression
    ;

notOp
    : NOT
    | '!'
    ;


funcCall
    : (NON_DIGIT | builtin_func) (DIGIT | NON_DIGIT)*
    ;

firstPrecedenceMathOperator
    : '*' | '/' | '**' | '%' | POW | MUL | DIV | MOD
    ;

secondPrecedenceMathOperator
    : '+' | '-' | ADD | SUB
    ;

compareOperator
    : '>' | '>=' | '<' | '<=' | '='
    | '==' | '!='
    ;

logicalXor
    : XOR | '^' '|'
    ;

logicalAnd
    : AND | '&' '&'
    ;

logicalOr
    : OR | '|' '|'
    ;


functionArgs
    : expression (',' expression)* ','?
    ;


identifier
    : (NON_DIGIT | builtin_func) (DIGIT | NON_DIGIT)*
    ;

sign : '+' | '-'
     ;

integerLiteral
    : DIGIT+ ;


floatLiteral
    : DIGIT+ '.' DIGIT+
    ;

decimalLiteral
    : integerLiteral
    | floatLiteral
    ;

stringLiteral
    : DQUOTA_STRING
    | SQUOTA_STRING
    ;


DIGIT : [0-9];
NON_DIGIT : [a-zA-Z_];

//单引号和双引号字符串
DQUOTA_STRING:              '"' ( '\\'. | '""' | ~('"'| '\\') )* '"';
SQUOTA_STRING:              '\'' ('\\'. | '\'\'' | ~('\'' | '\\'))* '\'';


builtin_func
    : ADD | MOD | SUB | MUL | DIV | POW
    | AND | NOT | OR | XOR
    ;


ADD : 'ADD' | 'add';
MOD : 'MOD' | 'mod';
SUB : 'SUB' | 'sub';
MUL : 'MUL' | 'mul';
DIV : 'DIV' | 'div';
POW : 'POW' | 'pow';


AND : 'AND' | 'and';

NOT : 'NOT' | 'not';

OR : 'OR' | 'or';
XOR : 'XOR' | 'xor';


WS : [ \r\t\n]+ ->skip;




