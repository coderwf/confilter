# -*- coding: utf-8 -*-
from cfilter.funcs.service import FuncService


class TestFuncService:
    # 测试内置函数
    def test_builtin_func(self):
        assert FuncService.exec("+", 1, 2) == 3
        assert FuncService.exec("Add", 1, 2) == 3

        assert FuncService.exec("-", 4, 2) == 2
        assert FuncService.exec("SuB", 4, 2) == 2

        assert FuncService.exec("*", 4, 5) == 20
        assert FuncService.exec("muL", 4, 5) == 20

        assert FuncService.exec("Div", 4, 2) == 2.0
        assert FuncService.exec("/", 4, 2) == 2.0

        assert FuncService.exec("Pow", 2, 3) == 8
        assert FuncService.exec("**", 2, 3) == 8

        assert FuncService.exec("round", 2.22, 1) == 2.2

        assert FuncService.exec("moD", 5, 2) == 1
        assert FuncService.exec("%", 5, 2) == 1

        assert FuncService.exec("And", True, False) is False
        assert FuncService.exec("&&", True, False) is False

        assert FuncService.exec("Or", True, False) is True
        assert FuncService.exec("||", True, False) is True

        assert FuncService.exec("xor", True, True) is False
        assert FuncService.exec("^|", True, True) is False

        assert FuncService.exec("not", False) is True
        assert FuncService.exec("!", True) is False

        assert FuncService.exec(">", 4, 2) is True
        assert FuncService.exec(">=", 3, 3) is True

        assert FuncService.exec("<", 3, 4) is True
        assert FuncService.exec("<=", 3, 4) is True

        assert FuncService.exec("=", 3, 3) is True
        assert FuncService.exec("!=", 3, 3) is False

        assert FuncService.exec("is", 3, 3) is True
        assert FuncService.exec("isn't", 3, 3) is False

        assert FuncService.exec("==", 3, 3) is True
        assert FuncService.exec("int", 3.4) == 3
        assert FuncService.exec("float", "3.4") == 3.4
        assert FuncService.exec("str", 3) == "3"
        assert FuncService.exec("str", 3.5) == "3.5"

