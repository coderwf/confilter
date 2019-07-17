# -*- coding: utf-8 -*-
from cfilter.fantlr.CFilterVisitor import CFilterVisitor
from cfilter.fantlr.CFilterParser import CFilterParser
from cfilter.funcs.service import FuncService


class MyVisitor(CFilterVisitor):

    def __init__(self):
        super(CFilterVisitor, self).__init__()
        self.data_source = None

    def visit_res(self, tree, data_source=None):
        """

        :param tree:
        :param data_source:  dict {"employee_id": 1, "working_hour_type: 3}
        :return:
        """
        self.data_source = data_source
        return self.visit(tree)

    def visitCfilter(self, ctx: CFilterParser.CfilterContext):
        statement = ctx.expressionStatement()
        if statement is None:
            return True

        return self.visit(statement)

    def visitExpressionStatement(self, ctx: CFilterParser.ExpressionStatementContext):
        return self.visit(ctx.expression())

    # 带符号
    def visitSignedExpression(self, ctx: CFilterParser.SignedExpressionContext):
        expression_val = self.visit(ctx.expression())
        sign_text = ctx.sign().getText()
        return -expression_val if sign_text == '-' else expression_val

    # not expression
    def visitNotExpression(self, ctx: CFilterParser.NotExpressionContext):
        return not self.visit(ctx.expression())

    # 带括号
    def visitParentExpression(self, ctx: CFilterParser.ParentExpressionContext):
        return self.visit(ctx.expression())

    # 第一优先级运算
    def visitFpMathOperatorExpression(self, ctx: CFilterParser.FpMathOperatorExpressionContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        operator = ctx.firstPrecedenceMathOperator().getText()
        return FuncService.exec(operator, left, right)

    # 第二优先级运算
    def visitSpMathOperatorExpression(self, ctx: CFilterParser.SpMathOperatorExpressionContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        operator = ctx.secondPrecedenceMathOperator().getText()
        return FuncService.exec(operator, left, right)

    # 对比
    def visitCOperatorExpression(self, ctx: CFilterParser.COperatorExpressionContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        operator = ctx.compareOperator().getText()
        return FuncService.exec(operator, left, right)

    # 逻辑运算符
    def visitLogicAndExpression(self, ctx: CFilterParser.LogicAndExpressionContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        operator = ctx.logicalAnd().getText()
        return FuncService.exec(operator, left, right)

    def visitLogicXorExpression(self, ctx: CFilterParser.LogicXorExpressionContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        operator = ctx.logicalXor().getText()
        return FuncService.exec(operator, left, right)

    def visitLogicOrExpression(self, ctx: CFilterParser.LogicOrExpressionContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        operator = ctx.logicalOr().getText()
        return FuncService.exec(operator, left, right)

    # 函数调用
    def visitFunctionCallExpression(self, ctx: CFilterParser.FunctionCallExpressionContext):
        func_name = ctx.funcCall().getText()
        func_args = ctx.functionArgs()
        if func_args is None:
            return FuncService.exec(func_name)
        return FuncService.exec(func_name, *self.visit(func_args))

    def visitFunctionArgs(self, ctx: CFilterParser.FunctionArgsContext):
        return tuple(self.visit(expression) for expression in ctx.expression())

    # 数字
    def visitLiteralExpression(self, ctx: CFilterParser.LiteralExpressionContext):
        return self.visit(ctx.decimalLiteral())

    # 小数
    def visitFloatLiteral(self, ctx: CFilterParser.FloatLiteralContext):
        return float(ctx.getText())

    # 整数
    def visitIntegerLiteral(self, ctx: CFilterParser.IntegerLiteralContext):
        return int(ctx.getText())

    # 变量
    def visitIdentifier(self, ctx: CFilterParser.IdentifierContext):
        identifier = ctx.getText()
        if identifier not in self.data_source:
            raise Exception("undefined identifier %s" % identifier)
        return self.data_source.get(identifier)

    # 字符串
    def visitStrLiteralExpression(self, ctx: CFilterParser.StrLiteralExpressionContext):
        quote_string = ctx.getText()
        return quote_string[1: -1]



