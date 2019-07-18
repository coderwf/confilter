# -*- coding: utf-8 -*-
from cfilter.fantlr.CFilterVisitor import CFilterVisitor
from cfilter.fantlr.CFilter import CFilter
from cfilter.visitor.errors import FuncNotFound, IdentifierNotFound
from cfilter.funcs.service import FuncService
from cfilter.fantlr.CFLexer import CFLexer


class MyVisitor(CFilterVisitor):

    logic_op_map = {
        CFLexer.AND: "and",
        CFLexer.OR: "or",
        CFLexer.XOR: "xor",

    }

    def __init__(self):
        super(CFilterVisitor, self).__init__()
        self._data = None

    def visit_res(self, tree, data=None):
        """
        设置data,包含变量值
        :param tree:
        :param data: {"a": 1, "b": 3}
        :return:
        """
        self._data = data
        return self.visit(tree)

    def visitRoot(self, ctx: CFilter.RootContext):
        """

        :param ctx:
        :return: return True if empty
        """
        statement = ctx.statement()
        if statement is None:
            return True
        return self.visit(ctx.statement())

    def visitStatement(self, ctx: CFilter.StatementContext):
        """

        :param ctx:
        :return:
        """
        return self.visit(ctx.expression())

    def visitParentExpressionAtom(self, ctx: CFilter.ParentExpressionAtomContext):
        """

        :param ctx:
        :return:
        """
        return self.visit(ctx.statement())

    def visitNotExpression(self, ctx: CFilter.NotExpressionContext):
        """

        :param ctx:
        :return: not expression
        """
        value = self.visit(ctx.expression())
        return not value

    def visitLogicalExpression(self, ctx: CFilter.LogicalExpressionContext):
        """

        :param ctx:
        :return: expression logicalOp expression
        """
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        operator = self.logic_op_map.get(ctx.logicalOp.type)
        if not FuncService.exists(operator):
            raise FuncNotFound(operator)
        return FuncService.exec(operator, left, right)

    def visitIsExpression(self, ctx: CFilter.IsExpressionContext):
        """

        :param ctx:
        :return: is expression
        """
        left = self.visit(ctx.predicate())
        right = self.visit(ctx.expression())

        if ctx.NOT() is None:
            return left is right
        return left is not right

    def visitPredicateExpression(self, ctx: CFilter.PredicateExpressionContext):
        """

        :param ctx:
        :return:
        """
        return self.visit(ctx.predicate())

    def visitInPredicate(self, ctx: CFilter.InPredicateContext):
        """

        :param ctx:
        :return: val in (1, 2, 3)
        """
        left = self.visit(ctx.predicate())
        right = self.visit(ctx.expressions())
        if ctx.NOT() is None:
            return left in right
        return left not in right

    def visitExpressions(self, ctx: CFilter.ExpressionsContext):
        expressions = tuple(self.visit(expression) for expression in ctx.expression())
        return expressions

    def visitBinaryComparasionPredicate(self, ctx: CFilter.BinaryComparasionPredicateContext):
        """

        :param ctx:
        :return:
        """
        operator = ctx.comparisonOperator().getText()
        left = self.visit(ctx.predicate(0))
        right = self.visit(ctx.predicate(1))
        if not FuncService.exists(operator):
            raise FuncNotFound(operator)
        return FuncService.exec(operator, left, right)

    def visitExpressionAtomPredicate(self, ctx: CFilter.ExpressionAtomPredicateContext):
        """

        :param ctx:
        :return:
        """
        return self.visit(ctx.expressionAtom())

    def visitConstantExpressionAtom(self, ctx: CFilter.ConstantExpressionAtomContext):
        return self.visit(ctx.constant())

    def visitConstant(self, ctx: CFilter.ConstantContext):
        if ctx.stringLiteral() is not None:
            return ctx.getText()[1: -1]

        val = self.visit(ctx.decimalLiteral())
        if ctx.getText().startswith("-"):
            return -val
        return val

    def visitDecimalLiteral(self, ctx: CFilter.DecimalLiteralContext):
        """

        :param ctx:
        :return:
        """
        str_val = ctx.getText()
        if ctx.INTEGER_LITERAL() is not None:
            return int(str_val)
        return float(str_val)

    def visitIdentifierExpressionAtom(self, ctx: CFilter.IdentifierExpressionAtomContext):
        """

        :param ctx:
        :return:
        """
        identifier = ctx.getText()
        val = self._data and self._data.get(identifier, None)
        if val is None:
            raise IdentifierNotFound(identifier)
        return val

    def visitFunctionCallExpressionAtom(self, ctx: CFilter.FunctionCallExpressionAtomContext):
        """

        :param ctx:
        :return:
        """
        return self.visit(ctx.functionCall())

    def visitFunctionCall(self, ctx: CFilter.FunctionCallContext):
        """

        :param ctx:
        :return:
        """
        func_name = ctx.ID_LITERAL().getText()
        args = self.visit(ctx.functionArgs())
        if not FuncService.exists(func_name):
            raise FuncNotFound(func_name)
        return FuncService.exec(func_name, *args)

    def visitFunctionArgs(self, ctx: CFilter.FunctionArgsContext):
        """

        :param ctx:
        :return:
        """
        function_args = tuple(self.visit(function_arg) for function_arg in ctx.functionArg())
        return function_args

    def visitFunctionArg(self, ctx: CFilter.FunctionArgContext):
        """

        :param ctx:
        :return:
        """
        if ctx.constant():
            return self.visit(ctx.constant())
        elif ctx.expression():
            return self.visit(ctx.expression())
        else:
            return self.visit(ctx.functionCall())

    def visitUnaryExpressionAtom(self, ctx: CFilter.UnaryExpressionAtomContext):
        """

        :param ctx:
        :return:
        """
        operator = ctx.unaryOperator().getText()
        expr_val = self.visit(ctx.expressionAtom())
        if not FuncService.exists(operator):
            raise FuncNotFound(operator)
        return FuncService.exec(operator, expr_val)

    def visitFmathExpressionAtom(self, ctx: CFilter.FmathExpressionAtomContext):
        """

        :param ctx:
        :return:
        """
        operator = ctx.fMathOperator().getText()
        left = self.visit(ctx.expressionAtom(0))
        right = self.visit(ctx.expressionAtom(1))
        if not FuncService.exists(operator):
            raise FuncNotFound(operator)
        return FuncService.exec(operator, left, right)

    def visitSmathExpressionAtom(self, ctx: CFilter.SmathExpressionAtomContext):
        """

        :param ctx:
        :return:
        """
        operator = ctx.sMathOperator().getText()
        left = self.visit(ctx.expressionAtom(0))
        right = self.visit(ctx.expressionAtom(1))
        if not FuncService.exists(operator):
            raise FuncNotFound(operator)
        return FuncService.exec(operator, left, right)

