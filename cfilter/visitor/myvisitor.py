# -*- coding: utf-8 -*-
from cfilter.fantlr.CFilterVisitor import CFilterVisitor
from cfilter.fantlr.CFilter import CFilter
from cfilter.fantlr.CFLexer import CFLexer
from cfilter.visitor.nodes import *


class MyVisitor(CFilterVisitor):

    logic_op_map = {
        CFLexer.AND: "and",
        CFLexer.OR: "or",
        CFLexer.XOR: "xor",

    }

    def __init__(self):
        self._identifiers = set()
        self._visited = False
        self._node = None

    def visit_res(self, tree):
        if self._visited:
            return self._identifiers, self._node
        self._visited = True
        _, self._node = self.visit(tree)
        return self._identifiers, self._node

    # 返回identifier个数和node结点
    # 如果identifier个数为0则node结点为常量
    def visitRoot(self, ctx: CFilter.RootContext):
        """

        :param ctx:
        :return: return True if empty str
        """
        statement = ctx.statement()
        self._visited = True
        if statement is None:
            return 0, Const(True)
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
        count, expr_node = self.visit(ctx.expression())
        if count == 0:
            return 0, Const(not expr_node.visit())
        return count, Func("not", expr_node)

    def visitLogicalExpression(self, ctx: CFilter.LogicalExpressionContext):
        """

        :param ctx:
        :return: expression logicalOp expression
        """
        left_count, left_node = self.visit(ctx.expression(0))
        right_count, right_node = self.visit(ctx.expression(1))
        logic_operator = self.logic_op_map.get(ctx.logicalOp.type)
        # xor必须计算两边
        if logic_operator == "xor":
            return left_count + right_count, Func("xor", left_node, right_node)

        # 如果左右表达式包含变量,则只能返回node结点
        if left_count != 0 and right_count != 0:
            if logic_operator == "and":
                return left_count + right_count, AndFunc(left_node, right_node)
            else:
                return left_count + right_count, OrFunc(left_node, right_node)

        if left_count == 0 and right_count == 0:
            return 0, Const(FuncService.exec(logic_operator, left_node.visit(), right_node.visit()))

        if logic_operator == "and":
            if left_count == 0 and bool(left_node.visit()) is False:
                return 0, Const(False)
            if right_count == 0 and bool(right_node.visit()) is False:
                return 0, Const(False)
            # 结果只取决于某一个值
            return (right_count, Func("bool", right_node)) if left_count == 0 else (left_count, Func("bool", left_node))

        # or
        if left_count == 0 and bool(left_node.visit()) is True:
            return 0, Const(True)

        if right_count == 0 and bool(right_node.visit()) is True:
            return 0, Const(True)

        # bool表达式已知一个数则结果只取决于另一个数
        return (right_count, Func("bool", right_node)) if left_count == 0 else (right_count, Func("bool", right_node))

    def visitIsExpression(self, ctx: CFilter.IsExpressionContext):
        """

        :param ctx:
        :return: is expression
        """
        left_count, left_node = self.visit(ctx.predicate())
        right_count, right_node = self.visit(ctx.expression())
        not_id = True if ctx.NOT() else False
        if left_count + right_count == 0:
            res_node = Const(left_node.visit() is not right_node.visit()) if not_id else \
                Const(left_node.visit() is right_node.visit())
            return 0, res_node
        func = "is_not" if not_id else "is"
        return left_count + right_count, Func(func, left_node, right_node)

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
        left_count, left_node = self.visit(ctx.predicate())
        right_count, right_node = self.visit(ctx.expressions())
        not_id = True if ctx.NOT() else False
        if left_count + right_count == 0:
            res_node = Const(left_node.visit() not in right_node.visit()) if not_id else \
                Const(left_node.visit() in right_node.visit())
            return 0, res_node

        func = "not_in" if not_id else "in"
        return left_count + right_count, Func(func, left_node, right_node)

    def visitExpressions(self, ctx: CFilter.ExpressionsContext):
        id_count = 0
        nodes = []
        for expr in ctx.expression():
            count, node = self.visit(expr)
            id_count += count
            nodes.append(node)
        if id_count == 0:
            return 0, Consts(tuple(node.visit() for node in nodes))
        return id_count, Exps(nodes)

    def visitBinaryComparasionPredicate(self, ctx: CFilter.BinaryComparasionPredicateContext):
        """

        :param ctx:
        :return:
        """
        operator = ctx.comparisonOperator().getText()
        left_count, left_node = self.visit(ctx.predicate(0))
        right_count, right_node = self.visit(ctx.predicate(1))
        if left_count + right_count == 0:
            return 0, Const(FuncService.exec(operator, left_node.visit(), right_node.visit()))

        return left_count + right_count, Func(operator, left_node, right_node)

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
            return 0, Const(ctx.getText()[1: -1])

        val = self.visit(ctx.decimalLiteral())
        if ctx.getText().startswith("-"):
            return 0, Const(-val)
        return 0, Const(val)

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
        self._identifiers.add(identifier)
        return 1, Identifier(identifier)

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
        count, nodes = self.visit(ctx.functionArgs())
        if count == 0:
            return 0, Consts(FuncService.exec(func_name, *tuple(node.visit() for node in nodes)))
        return count, Func(func_name, *tuple(nodes))

    def visitFunctionArgs(self, ctx: CFilter.FunctionArgsContext):
        """

        :param ctx:
        :return:
        """
        id_count = 0
        nodes = []
        for fg in ctx.functionArg():
            count, node = self.visit(fg)
            id_count += count
            nodes.append(node)
        return id_count, nodes

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
        count, node = self.visit(ctx.expressionAtom())
        if count == 0:
            return 0, Const(FuncService.exec(operator, node.visit()))
        return count, Func(operator, node)

    def visitFmathExpressionAtom(self, ctx: CFilter.FmathExpressionAtomContext):
        """

        :param ctx:
        :return:
        """
        operator = ctx.fMathOperator().getText()
        left_count, left_node = self.visit(ctx.expressionAtom(0))
        right_count, right_node = self.visit(ctx.expressionAtom(1))
        if left_count + right_count == 0:
            return 0, Const(FuncService.exec(operator, left_node.visit(), right_node.visit()))
        return left_count + right_count, Func(operator, left_node, right_node)

    def visitSmathExpressionAtom(self, ctx: CFilter.SmathExpressionAtomContext):
        """

        :param ctx:
        :return:
        """
        operator = ctx.sMathOperator().getText()
        left_count, left_node = self.visit(ctx.expressionAtom(0))
        right_count, right_node = self.visit(ctx.expressionAtom(1))
        if left_count + right_count == 0:
            return 0, Const(FuncService.exec(operator, left_node.visit(), right_node.visit()))
        return left_count + right_count, Func(operator, left_node, right_node)
