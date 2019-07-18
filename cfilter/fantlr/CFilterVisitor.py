# Generated from ../cfilter/fantlr/CFilter.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CFilter import CFilter
else:
    from CFilter import CFilter

# This class defines a complete generic visitor for a parse tree produced by CFilter.

class CFilterVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CFilter#root.
    def visitRoot(self, ctx:CFilter.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilter#statement.
    def visitStatement(self, ctx:CFilter.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilter#stringLiteral.
    def visitStringLiteral(self, ctx:CFilter.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilter#decimalLiteral.
    def visitDecimalLiteral(self, ctx:CFilter.DecimalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilter#constant.
    def visitConstant(self, ctx:CFilter.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilter#identifier.
    def visitIdentifier(self, ctx:CFilter.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilter#functionArg.
    def visitFunctionArg(self, ctx:CFilter.FunctionArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilter#functionArgs.
    def visitFunctionArgs(self, ctx:CFilter.FunctionArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilter#functionCall.
    def visitFunctionCall(self, ctx:CFilter.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilter#expressions.
    def visitExpressions(self, ctx:CFilter.ExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilter#isExpression.
    def visitIsExpression(self, ctx:CFilter.IsExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilter#notExpression.
    def visitNotExpression(self, ctx:CFilter.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilter#logicalExpression.
    def visitLogicalExpression(self, ctx:CFilter.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilter#predicateExpression.
    def visitPredicateExpression(self, ctx:CFilter.PredicateExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilter#expressionAtomPredicate.
    def visitExpressionAtomPredicate(self, ctx:CFilter.ExpressionAtomPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilter#inPredicate.
    def visitInPredicate(self, ctx:CFilter.InPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilter#binaryComparasionPredicate.
    def visitBinaryComparasionPredicate(self, ctx:CFilter.BinaryComparasionPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilter#smathExpressionAtom.
    def visitSmathExpressionAtom(self, ctx:CFilter.SmathExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilter#unaryExpressionAtom.
    def visitUnaryExpressionAtom(self, ctx:CFilter.UnaryExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilter#constantExpressionAtom.
    def visitConstantExpressionAtom(self, ctx:CFilter.ConstantExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilter#functionCallExpressionAtom.
    def visitFunctionCallExpressionAtom(self, ctx:CFilter.FunctionCallExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilter#fmathExpressionAtom.
    def visitFmathExpressionAtom(self, ctx:CFilter.FmathExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilter#identifierExpressionAtom.
    def visitIdentifierExpressionAtom(self, ctx:CFilter.IdentifierExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilter#parentExpressionAtom.
    def visitParentExpressionAtom(self, ctx:CFilter.ParentExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilter#unaryOperator.
    def visitUnaryOperator(self, ctx:CFilter.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilter#comparisonOperator.
    def visitComparisonOperator(self, ctx:CFilter.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilter#logicalOperator.
    def visitLogicalOperator(self, ctx:CFilter.LogicalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilter#fMathOperator.
    def visitFMathOperator(self, ctx:CFilter.FMathOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFilter#sMathOperator.
    def visitSMathOperator(self, ctx:CFilter.SMathOperatorContext):
        return self.visitChildren(ctx)



del CFilter