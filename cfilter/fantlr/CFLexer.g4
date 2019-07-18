// CFLexer.g4

lexer grammar CFLexer;

channels {ERRORCHANNEL }

//Skip
SPACE:                               [ \t\r\n]+    -> channel(HIDDEN);


// Fragments
//语法不区分大小写
fragment A          : ('A'|'a') ;
fragment B          : ('B'|'b') ;
fragment C          : ('C'|'c') ;
fragment D          : ('D'|'d') ;
fragment E          : ('E'|'e') ;
fragment F          : ('F'|'f') ;
fragment G          : ('G'|'g') ;
fragment H          : ('H'|'h') ;
fragment I          : ('I'|'i') ;
fragment J          : ('J'|'j') ;
fragment K          : ('K'|'k') ;
fragment L          : ('L'|'l') ;
fragment M          : ('M'|'m') ;
fragment N          : ('N'|'n') ;
fragment O          : ('O'|'o') ;
fragment P          : ('P'|'p') ;
fragment Q          : ('Q'|'q') ;
fragment R          : ('R'|'r') ;
fragment S          : ('S'|'s') ;
fragment T          : ('T'|'t') ;
fragment U          : ('U'|'u') ;
fragment V          : ('V'|'v') ;
fragment W          : ('W'|'w') ;
fragment X          : ('X'|'x') ;
fragment Y          : ('Y'|'y') ;
fragment Z          : ('Z'|'z') ;




IN : I N;

//+-*/% **
ADD : A D D;
SUB : S U B;
MUL : M U L;
DIV : D I V;
MOD : M O D;
POW : P O W;

// AND OR NOT XOR
AND : A N D | '&' '&';
OR : O R | '|' '|';
NOT : N O T;
XOR : X O R | '^' '|';

//func
ROUND: R O U N D;
INT: I N T;
FLOAT: F L O A T;
STR: S T R;

IS: I S;
IS_NOT: I S '_' N O T;

//math func
ABS: A B S;


// Operators. Arithmetics

STAR:                                '*';
DIVIDE:                              '/';
MODULE:                              '%';
PLUS:                                '+';
MINUS:                               '-';

// Operators. Bit

BIT_NOT_OP:                          '~';
BIT_OR_OP:                           '|';
BIT_AND_OP:                          '&';
BIT_XOR_OP:                          '^';


// Operators. Comparation

EQUAL_SYMBOL:                        '=';
GREATER_SYMBOL:                      '>';
LESS_SYMBOL:                         '<';
EXCLAMATION_SYMBOL:                  '!';


// Constructors symbols

DOT:                                 '.';
LR_BRACKET:                          '(';
RR_BRACKET:                          ')';
COMMA:                               ',';
SEMI :                               ';';



STRING_LITERAL:                      DQUOTA_STRING | SQUOTA_STRING | BQUOTA_STRING;
INTEGER_LITERAL:                     DEC_DIGIT+;
FLOAT_LITERAL:                       DEC_DIGIT+ '.' DEC_DIGIT+;

//IDENTIFIER
ID_LITERAL:                          [A-Z_a-z]+?[A-Z_0-9a-z]*;

//字符串
fragment DQUOTA_STRING:              '"' ( '\\'. | '""' | ~('"'| '\\') )* '"';
fragment SQUOTA_STRING:              '\'' ('\\'. | '\'\'' | ~('\'' | '\\'))* '\'';
fragment BQUOTA_STRING:              '`' ( '\\'. | '``' | ~('`'|'\\'))* '`';

//十六进制数字
fragment HEX_DIGIT:                  [0-9A-F];

//数字
fragment DEC_DIGIT:                  [0-9];


ERROR_RECONGNIGION:                  .    -> channel(ERRORCHANNEL);