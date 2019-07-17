# -*- coding: utf-8 -*-
from cfilter.filter import Filter
from cfilter.funcs.service import FuncService


class TestVisitor:
    # 标志符(变量)
    def test_identifier(self):
        assert Filter("name").visit_res({"name": "jack"}) == "jack"
        assert Filter("age").visit_res({"age": 12}) == 12
        assert Filter("add1").visit_res({"add1": 30}) == 30

    # 字符串
    def test_string_literal(self):
        assert Filter("\"jack\"").visit_res() == "jack"
        assert Filter("'jack'").visit_res() == "jack"
        assert Filter("'中文'").visit_res() == "中文"

    # 数字
    def test_decimal_literal(self):
        assert Filter("3.44").visit_res() == 3.44
        assert Filter("3").visit_res() == 3
        assert Filter("3.0").visit_res() == 3.0
        assert Filter("4.455").visit_res() == 4.455

    # 函数调用
    def test_func_call(self):
        FuncService.register("add3", lambda x, y, z: x + y + z)
        assert Filter("add3(1, 2, 3)").visit_res() == 6
        assert Filter("add3(b, 4, c)").visit_res({"b": 4, "c": 5}) == 13
        FuncService.unregister("div4")

    # 逻辑表达式
    def test_logical_expression(self):
        assert Filter("0 and 0").visit_res() is False
        assert Filter("1 and 0").visit_res() is False
        assert Filter("1 and 1").visit_res() is True
        assert Filter("0 && 0").visit_res() is False
        assert Filter("1 or 1").visit_res() is True
        assert Filter("1 or 0").visit_res() is True
        assert Filter("1 || 0").visit_res() is True
        assert Filter("not 1").visit_res() is False
        assert Filter("not 0").visit_res() is True
        assert Filter("! 0").visit_res() is True

    # 比较表达式
    def test_compare_expression(self):
        assert Filter("3 > 2").visit_res() is True
        assert Filter("3 <= 2").visit_res() is False
        assert Filter("3 != 2").visit_res() is True
        assert Filter("3 == 2").visit_res() is False
        assert Filter("3 <= 2").visit_res() is False
        assert Filter("3 > 3").visit_res() is False
        assert Filter("3 > 2").visit_res() is True

    # 四则运算
    def test_math_expression(self):
        assert Filter("1 + 2 + 4 * 5").visit_res() == 23
        assert Filter("3 * 5 + 4").visit_res() == 19
        assert Filter("1 + 1.5 + 3 + (2 + 4)*2 + 4*3").visit_res() == 29.5
        assert Filter("a + b * c +d").visit_res({"a": 1, "b": 3, "c": 3, "d": 4}) == 14

    # 优先级
    def test_priority(self):
        assert Filter("1 + 2 * 4 + 2").visit_res() == 11
        assert Filter("3 * (4 + 5) / 3").visit_res() == 9
        assert Filter("1 + 3 > 2").visit_res() is True
        assert Filter("2 * 4 < 3").visit_res() is False
        assert Filter("0 and 1 or not 1").visit_res() is False
        assert Filter("(0 and 1) or (not 1)").visit_res() is False
        assert Filter("").visit_res() is True
        assert Filter("1 or 1 and 0").visit_res() is True

        assert Filter("not not not 1").visit_res() is False
        assert Filter("1 and 0 or 1 and 0").visit_res() is False

        assert Filter("not 1 or 1").visit_res() is True
        assert Filter("not (1 or 1)").visit_res() is False

        assert Filter("not 0 and 0").visit_res() is False
        assert Filter("not (0 and 0)").visit_res() is True

        assert Filter("1 + 3 and 0").visit_res() is False
        assert Filter("1 * 3 and 0").visit_res() is False

        assert Filter("3 > 1 and 0").visit_res() is False
        assert Filter("3 > 1 and 1").visit_res() is True
        assert Filter("3 > 1 or 0").visit_res() is True

        assert Filter("3 > 1 and 4 > 2").visit_res() is True
        assert Filter("3 + 4 < 5 and 2 + 1 < 2").visit_res() is False
        assert Filter("3 + 4 < 5 or 2 + 1 > 2").visit_res() is True

    # 括号嵌套
    def test_parents_expr(self):
        assert Filter("not (not (not (1)))").visit_res() is False
        assert Filter("((1+2)*3 + (2+3)*5)*2").visit_res() == 68
        assert Filter("(4*5+2)%3").visit_res() == 1
        assert Filter("5 % 3 * (2 + 1)").visit_res() == 6