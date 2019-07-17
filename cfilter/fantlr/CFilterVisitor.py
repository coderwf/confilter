# Generated from ../cfilter/fantlr/CFilter.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CFilterParser import CFilterParser
else:
    from CFilterParser import CFilterParser

# This class defines a complete generic visitor for a parse tree produced by CFilterParser.

class CFilterVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CFilterParser#cfilter.
    def visitCfilter(self, ctx:CFilterParser.CfilterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#expressionStatement.
    def visitExpressionStatement(self, ctx:CFilterParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#strLiteralExpression.
    def visitStrLiteralExpression(self, ctx:CFilterParser.StrLiteralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#identifierExpression.
    def visitIdentifierExpression(self, ctx:CFilterParser.IdentifierExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#logicXorExpression.
    def visitLogicXorExpression(self, ctx:CFilterParser.LogicXorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#notExpression.
    def visitNotExpression(self, ctx:CFilterParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#spMathOperatorExpression.
    def visitSpMathOperatorExpression(self, ctx:CFilterParser.SpMathOperatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#parentExpression.
    def visitParentExpression(self, ctx:CFilterParser.ParentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#cOperatorExpression.
    def visitCOperatorExpression(self, ctx:CFilterParser.COperatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#logicAndExpression.
    def visitLogicAndExpression(self, ctx:CFilterParser.LogicAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#signedExpression.
    def visitSignedExpression(self, ctx:CFilterParser.SignedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#logicOrExpression.
    def visitLogicOrExpression(self, ctx:CFilterParser.LogicOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#fpMathOperatorExpression.
    def visitFpMathOperatorExpression(self, ctx:CFilterParser.FpMathOperatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#functionCallExpression.
    def visitFunctionCallExpression(self, ctx:CFilterParser.FunctionCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#literalExpression.
    def visitLiteralExpression(self, ctx:CFilterParser.LiteralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#notOp.
    def visitNotOp(self, ctx:CFilterParser.NotOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#funcCall.
    def visitFuncCall(self, ctx:CFilterParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#firstPrecedenceMathOperator.
    def visitFirstPrecedenceMathOperator(self, ctx:CFilterParser.FirstPrecedenceMathOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#secondPrecedenceMathOperator.
    def visitSecondPrecedenceMathOperator(self, ctx:CFilterParser.SecondPrecedenceMathOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#compareOperator.
    def visitCompareOperator(self, ctx:CFilterParser.CompareOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#logicalXor.
    def visitLogicalXor(self, ctx:CFilterParser.LogicalXorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#logicalAnd.
    def visitLogicalAnd(self, ctx:CFilterParser.LogicalAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#logicalOr.
    def visitLogicalOr(self, ctx:CFilterParser.LogicalOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#functionArgs.
    def visitFunctionArgs(self, ctx:CFilterParser.FunctionArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#identifier.
    def visitIdentifier(self, ctx:CFilterParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#sign.
    def visitSign(self, ctx:CFilterParser.SignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#integerLiteral.
    def visitIntegerLiteral(self, ctx:CFilterParser.IntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#floatLiteral.
    def visitFloatLiteral(self, ctx:CFilterParser.FloatLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#decimalLiteral.
    def visitDecimalLiteral(self, ctx:CFilterParser.DecimalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#stringLiteral.
    def visitStringLiteral(self, ctx:CFilterParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilterParser#builtin_func.
    def visitBuiltin_func(self, ctx:CFilterParser.Builtin_funcContext):
        return self.visitChildren(ctx)



del CFilterParser