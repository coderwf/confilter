parser grammar CFilter;

options { tokenVocab=CFLexer; }


root
    : statement ? EOF
    ;


statement
    : expression SEMI?
    ;


stringLiteral
    : STRING_LITERAL
    ;


decimalLiteral
    : INTEGER_LITERAL
    | FLOAT_LITERAL
    ;


constant
    : stringLiteral | decimalLiteral
    | '-' decimalLiteral
    ;


identifier
    : ID_LITERAL
    ;


functionArg
    : constant
    | functionCall
    | expression
    ;


functionArgs
    : functionArg
    (
      ','
      functionArg
    )*
    ;


functionCall
    : ID_LITERAL '(' functionArgs ')'
    ;


expressions
    : expression (',' expression)*
    ;


expression
    : notOperator=(NOT | '!') expression                            # notExpression
    | expression logicalOp=XOR expression                           # logicalExpression
    | expression logicalOp=AND expression                           # logicalExpression
    | expression logicalOp=OR expression                            # logicalExpression
    | predicate IS NOT? expression                                  # isExpression
    | predicate                                                     # predicateExpression
    ;


predicate
    : predicate NOT? IN '(' expressions ')'                         # inPredicate
    | left=predicate comparisonOperator right=predicate             # binaryComparasionPredicate
    | expressionAtom                                                # expressionAtomPredicate
    ;


// Add in ASTVisitor nullNotnull in constant
expressionAtom
    : constant                                                      # constantExpressionAtom
    | identifier                                                    # identifierExpressionAtom
    | functionCall                                                  # functionCallExpressionAtom
    | unaryOperator expressionAtom                                  # unaryExpressionAtom
    | '(' statement ')'                                             # parentExpressionAtom
    | left=expressionAtom fMathOperator right=expressionAtom        # fmathExpressionAtom
    | left=expressionAtom sMathOperator right=expressionAtom        # smathExpressionAtom
    ;



unaryOperator
    : '!' | '~' | '+' | '-' | NOT
    ;


comparisonOperator
    : '=' | '>' | '<' | '<' '=' | '>' '='
    | '<' '>' | '!' '=' | '<' '=' '>'
    | '=' '=' | IS | IS_NOT
    ;


//xor > and > or
logicalOperator
    : AND | '&' '&' | XOR | OR | '|' '|'
    ;


fMathOperator
    : '*'| '/' | MUL | DIV | '%' | MOD
    ;


sMathOperator
    : '+' | '-' | ADD | SUB
    ;

