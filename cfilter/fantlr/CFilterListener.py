# Generated from ../cfilter/fantlr/CFilter.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CFilterParser import CFilterParser
else:
    from CFilterParser import CFilterParser

# This class defines a complete listener for a parse tree produced by CFilterParser.
class CFilterListener(ParseTreeListener):

    # Enter a parse tree produced by CFilterParser#cfilter.
    def enterCfilter(self, ctx:CFilterParser.CfilterContext):
        pass

    # Exit a parse tree produced by CFilterParser#cfilter.
    def exitCfilter(self, ctx:CFilterParser.CfilterContext):
        pass


    # Enter a parse tree produced by CFilterParser#expressionStatement.
    def enterExpressionStatement(self, ctx:CFilterParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by CFilterParser#expressionStatement.
    def exitExpressionStatement(self, ctx:CFilterParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by CFilterParser#strLiteralExpression.
    def enterStrLiteralExpression(self, ctx:CFilterParser.StrLiteralExpressionContext):
        pass

    # Exit a parse tree produced by CFilterParser#strLiteralExpression.
    def exitStrLiteralExpression(self, ctx:CFilterParser.StrLiteralExpressionContext):
        pass


    # Enter a parse tree produced by CFilterParser#identifierExpression.
    def enterIdentifierExpression(self, ctx:CFilterParser.IdentifierExpressionContext):
        pass

    # Exit a parse tree produced by CFilterParser#identifierExpression.
    def exitIdentifierExpression(self, ctx:CFilterParser.IdentifierExpressionContext):
        pass


    # Enter a parse tree produced by CFilterParser#logicXorExpression.
    def enterLogicXorExpression(self, ctx:CFilterParser.LogicXorExpressionContext):
        pass

    # Exit a parse tree produced by CFilterParser#logicXorExpression.
    def exitLogicXorExpression(self, ctx:CFilterParser.LogicXorExpressionContext):
        pass


    # Enter a parse tree produced by CFilterParser#notExpression.
    def enterNotExpression(self, ctx:CFilterParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by CFilterParser#notExpression.
    def exitNotExpression(self, ctx:CFilterParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by CFilterParser#spMathOperatorExpression.
    def enterSpMathOperatorExpression(self, ctx:CFilterParser.SpMathOperatorExpressionContext):
        pass

    # Exit a parse tree produced by CFilterParser#spMathOperatorExpression.
    def exitSpMathOperatorExpression(self, ctx:CFilterParser.SpMathOperatorExpressionContext):
        pass


    # Enter a parse tree produced by CFilterParser#parentExpression.
    def enterParentExpression(self, ctx:CFilterParser.ParentExpressionContext):
        pass

    # Exit a parse tree produced by CFilterParser#parentExpression.
    def exitParentExpression(self, ctx:CFilterParser.ParentExpressionContext):
        pass


    # Enter a parse tree produced by CFilterParser#cOperatorExpression.
    def enterCOperatorExpression(self, ctx:CFilterParser.COperatorExpressionContext):
        pass

    # Exit a parse tree produced by CFilterParser#cOperatorExpression.
    def exitCOperatorExpression(self, ctx:CFilterParser.COperatorExpressionContext):
        pass


    # Enter a parse tree produced by CFilterParser#logicAndExpression.
    def enterLogicAndExpression(self, ctx:CFilterParser.LogicAndExpressionContext):
        pass

    # Exit a parse tree produced by CFilterParser#logicAndExpression.
    def exitLogicAndExpression(self, ctx:CFilterParser.LogicAndExpressionContext):
        pass


    # Enter a parse tree produced by CFilterParser#signedExpression.
    def enterSignedExpression(self, ctx:CFilterParser.SignedExpressionContext):
        pass

    # Exit a parse tree produced by CFilterParser#signedExpression.
    def exitSignedExpression(self, ctx:CFilterParser.SignedExpressionContext):
        pass


    # Enter a parse tree produced by CFilterParser#logicOrExpression.
    def enterLogicOrExpression(self, ctx:CFilterParser.LogicOrExpressionContext):
        pass

    # Exit a parse tree produced by CFilterParser#logicOrExpression.
    def exitLogicOrExpression(self, ctx:CFilterParser.LogicOrExpressionContext):
        pass


    # Enter a parse tree produced by CFilterParser#fpMathOperatorExpression.
    def enterFpMathOperatorExpression(self, ctx:CFilterParser.FpMathOperatorExpressionContext):
        pass

    # Exit a parse tree produced by CFilterParser#fpMathOperatorExpression.
    def exitFpMathOperatorExpression(self, ctx:CFilterParser.FpMathOperatorExpressionContext):
        pass


    # Enter a parse tree produced by CFilterParser#functionCallExpression.
    def enterFunctionCallExpression(self, ctx:CFilterParser.FunctionCallExpressionContext):
        pass

    # Exit a parse tree produced by CFilterParser#functionCallExpression.
    def exitFunctionCallExpression(self, ctx:CFilterParser.FunctionCallExpressionContext):
        pass


    # Enter a parse tree produced by CFilterParser#literalExpression.
    def enterLiteralExpression(self, ctx:CFilterParser.LiteralExpressionContext):
        pass

    # Exit a parse tree produced by CFilterParser#literalExpression.
    def exitLiteralExpression(self, ctx:CFilterParser.LiteralExpressionContext):
        pass


    # Enter a parse tree produced by CFilterParser#notOp.
    def enterNotOp(self, ctx:CFilterParser.NotOpContext):
        pass

    # Exit a parse tree produced by CFilterParser#notOp.
    def exitNotOp(self, ctx:CFilterParser.NotOpContext):
        pass


    # Enter a parse tree produced by CFilterParser#funcCall.
    def enterFuncCall(self, ctx:CFilterParser.FuncCallContext):
        pass

    # Exit a parse tree produced by CFilterParser#funcCall.
    def exitFuncCall(self, ctx:CFilterParser.FuncCallContext):
        pass


    # Enter a parse tree produced by CFilterParser#firstPrecedenceMathOperator.
    def enterFirstPrecedenceMathOperator(self, ctx:CFilterParser.FirstPrecedenceMathOperatorContext):
        pass

    # Exit a parse tree produced by CFilterParser#firstPrecedenceMathOperator.
    def exitFirstPrecedenceMathOperator(self, ctx:CFilterParser.FirstPrecedenceMathOperatorContext):
        pass


    # Enter a parse tree produced by CFilterParser#secondPrecedenceMathOperator.
    def enterSecondPrecedenceMathOperator(self, ctx:CFilterParser.SecondPrecedenceMathOperatorContext):
        pass

    # Exit a parse tree produced by CFilterParser#secondPrecedenceMathOperator.
    def exitSecondPrecedenceMathOperator(self, ctx:CFilterParser.SecondPrecedenceMathOperatorContext):
        pass


    # Enter a parse tree produced by CFilterParser#compareOperator.
    def enterCompareOperator(self, ctx:CFilterParser.CompareOperatorContext):
        pass

    # Exit a parse tree produced by CFilterParser#compareOperator.
    def exitCompareOperator(self, ctx:CFilterParser.CompareOperatorContext):
        pass


    # Enter a parse tree produced by CFilterParser#logicalXor.
    def enterLogicalXor(self, ctx:CFilterParser.LogicalXorContext):
        pass

    # Exit a parse tree produced by CFilterParser#logicalXor.
    def exitLogicalXor(self, ctx:CFilterParser.LogicalXorContext):
        pass


    # Enter a parse tree produced by CFilterParser#logicalAnd.
    def enterLogicalAnd(self, ctx:CFilterParser.LogicalAndContext):
        pass

    # Exit a parse tree produced by CFilterParser#logicalAnd.
    def exitLogicalAnd(self, ctx:CFilterParser.LogicalAndContext):
        pass


    # Enter a parse tree produced by CFilterParser#logicalOr.
    def enterLogicalOr(self, ctx:CFilterParser.LogicalOrContext):
        pass

    # Exit a parse tree produced by CFilterParser#logicalOr.
    def exitLogicalOr(self, ctx:CFilterParser.LogicalOrContext):
        pass


    # Enter a parse tree produced by CFilterParser#functionArgs.
    def enterFunctionArgs(self, ctx:CFilterParser.FunctionArgsContext):
        pass

    # Exit a parse tree produced by CFilterParser#functionArgs.
    def exitFunctionArgs(self, ctx:CFilterParser.FunctionArgsContext):
        pass


    # Enter a parse tree produced by CFilterParser#identifier.
    def enterIdentifier(self, ctx:CFilterParser.IdentifierContext):
        pass

    # Exit a parse tree produced by CFilterParser#identifier.
    def exitIdentifier(self, ctx:CFilterParser.IdentifierContext):
        pass


    # Enter a parse tree produced by CFilterParser#sign.
    def enterSign(self, ctx:CFilterParser.SignContext):
        pass

    # Exit a parse tree produced by CFilterParser#sign.
    def exitSign(self, ctx:CFilterParser.SignContext):
        pass


    # Enter a parse tree produced by CFilterParser#integerLiteral.
    def enterIntegerLiteral(self, ctx:CFilterParser.IntegerLiteralContext):
        pass

    # Exit a parse tree produced by CFilterParser#integerLiteral.
    def exitIntegerLiteral(self, ctx:CFilterParser.IntegerLiteralContext):
        pass


    # Enter a parse tree produced by CFilterParser#floatLiteral.
    def enterFloatLiteral(self, ctx:CFilterParser.FloatLiteralContext):
        pass

    # Exit a parse tree produced by CFilterParser#floatLiteral.
    def exitFloatLiteral(self, ctx:CFilterParser.FloatLiteralContext):
        pass


    # Enter a parse tree produced by CFilterParser#decimalLiteral.
    def enterDecimalLiteral(self, ctx:CFilterParser.DecimalLiteralContext):
        pass

    # Exit a parse tree produced by CFilterParser#decimalLiteral.
    def exitDecimalLiteral(self, ctx:CFilterParser.DecimalLiteralContext):
        pass


    # Enter a parse tree produced by CFilterParser#stringLiteral.
    def enterStringLiteral(self, ctx:CFilterParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by CFilterParser#stringLiteral.
    def exitStringLiteral(self, ctx:CFilterParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by CFilterParser#builtin_func.
    def enterBuiltin_func(self, ctx:CFilterParser.Builtin_funcContext):
        pass

    # Exit a parse tree produced by CFilterParser#builtin_func.
    def exitBuiltin_func(self, ctx:CFilterParser.Builtin_funcContext):
        pass


