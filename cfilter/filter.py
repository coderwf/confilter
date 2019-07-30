# -*- coding: utf-8 -*-
import antlr4
from cfilter.fantlr.CFLexer import CFLexer
from cfilter.fantlr.CFilter import CFilter
from cfilter.visitor.myvisitor import MyVisitor
from cfilter.visitor.elistener import FilterErrorListener
from cfilter.funcs.service import FuncService
from cfilter.visitor.nodes import Func, OrFunc, AndFunc, Const, Node


class Filter:

    # 可以优化计算的func
    optimize_func = {"and", "or"}

    def __init__(self, rule, node=None, is_const=False, identifiers=None):
        """

        :param rule: 规则字符串 "a > 4 and a != b"
        :param node: 可以外部传入node(常数或者Node对象),此时不解析rule
        :param is_const: node是否为常数
        :param identifiers: 外部传入变量列表
        """

        self.rule = rule
        self.identifiers = identifiers
        self.node = node
        self.is_const = is_const

        # 需要根据rule自己解析node
        if self.node is None:
            self._parse_rule()

        # node为常量则visit_res不需要遍历结点,直接返回node即可

        elif is_const:
            self.__dict__["visit_res"] = lambda *args, **kwargs: self.node
        # node为Node结点则需要每次去遍历才能得到结果
        else:
            pass

    def _parse_rule(self):
        stream = antlr4.InputStream(self.rule)
        fl = CFLexer(stream)
        fl.removeErrorListeners()
        fl.addErrorListener(FilterErrorListener.INSTANCE)
        token_stream = antlr4.CommonTokenStream(fl)
        tree = CFilter(token_stream)
        tree.removeErrorListeners()
        tree.addErrorListener(FilterErrorListener.INSTANCE)
        visitor = MyVisitor()
        self.identifiers, self.node = visitor.visit_res(tree.root())

        # identifiers is None or len(self.identifiers) == 0
        # 表示表达式没有变量,所以可以直接计算出表达式的值
        # 此时可以提前计算表达式的值的函数更换visit_res为visit_const_res

        if self.identifiers is None or len(self.identifiers) == 0:
            self.node = self.node.visit()
            self.__dict__["visit_res"] = lambda *args, **kwargs: self.node
            self.is_const = True
        else:
            self.is_const = False

    @property
    def variables(self):
        return self.identifiers.copy()

    # 如果结果是个常量则需要直接返回结果
    def visit_res(self, value_map=None, **kwargs):
        return self.node.visit(value_map, **kwargs)

    def _filter_dict(self, sources, **kwargs):
        new_data_source = dict()
        for employee_id, source_dict in sources.items():
            ok = bool(self.visit_res(source_dict, **kwargs))
            if ok:
                new_data_source[employee_id] = source_dict

        return new_data_source

    def _filter_list(self, sources, **kwargs):
        new_data_source = []
        for source_dict in sources:
            ok = bool(self.visit_res(source_dict, **kwargs))
            if ok:
                new_data_source.append(source_dict)
        return new_data_source

    def filter(self, sources, **kwargs):
        if not isinstance(sources, (list, tuple, dict)):
            raise Exception("data_source must be (list, tuple, dict)")

        if isinstance(sources, dict):
            return self._filter_dict(sources, **kwargs)
        return self._filter_list(sources, **kwargs)

    # 通过func来join两个Filter
    def __join__(self, func, other):
        """
        Filter func Filter
        :param func: func_name (or, and, ...)
        :param other:
        :return:
        """
        # 新规则
        new_rule = '(' + self.rule + ') ' + func + " (" + other.rule + ")"
        new_identifiers = set()
        if self.identifiers:
            new_identifiers.update(self.identifiers)
        if other.identifiers:
            new_identifiers.update(other.identifiers)

        # 两个filter内部都是常量则可以直接计算
        if self.is_const and other.is_const:
            return Filter(new_rule, FuncService.exec(func, self.node, other.node), True, Node)

        if func not in self.optimize_func:
            if self.is_const:
                return Filter(new_rule, Func(func, Const(self.node), other.node), False, new_identifiers)
            if other.is_const:
                return Filter(new_rule, Func(func, self.node, Const(other.node)), False, new_identifiers)
            return Filter(new_rule, Func(func, self.node, other.node), False, new_identifiers)

        # 可以优化计算的func
        if not self.is_const and not other.is_const:
            if func == "and":
                return Filter(new_rule, AndFunc(self.node, other.node), False, new_identifiers)
            # or
            return Filter(new_rule, OrFunc(self.node, other.node), False, new_identifiers)

        if func == "and":
            if (self.is_const and not self.node) or (other.is_const and not other.node):
                return Filter(new_rule, False, True, new_identifiers)
            return Filter(new_rule, Func("bool", other.node), False, new_identifiers) if self.is_const else \
                Filter(new_rule, Func("bool", self.node), False, new_identifiers)

        # func == "or"
        if (self.is_const and self.node) or (other.is_const and other.node):
            return Filter(new_rule, True, True, new_identifiers)
        return Filter(new_rule, Func("bool", other.node), False, new_identifiers) if self.is_const else \
            Filter(new_rule, Func("bool", self.node),
    False, new_identifiers)

    def join(self, func, other):
        """

        :param func: func_name (or, and, ...)
        :param other: Filter
        :return:
        """
        return self.__join__(func, other)

    # filter对象间操作
    # + -
    def __add__(self, other):
        return self.__join__("+", other)

    def __sub__(self, other):
        return self.__join__("-", other)

    def __mul__(self, other):
        return self.__join__("*", other)

    def __truediv__(self, other):
        return self.__join__("/", other)

    def __and__(self, other):
        return self.__join__("and", other)

    def __or__(self, other):
        return self.__join__("or", other)

    def __xor__(self, other):
        return self.__join__("xor", other)

    def __gt__(self, other):
        return self.__join__(">", other)

    def __ge__(self, other):
        return self.__join__(">=", other)

    def __le__(self, other):
        return self.__join__("<=", other)

    def __lt__(self, other):
        return self.__join__("<", other)

    def __str__(self):
        return self.rule


if __name__ == "__main__":
    data_source = {
        100: {"eid": 100, "wht": 1, "et": "实习"},
        101: {"eid": 101, "wht": 2, "et": "实习"},
        102: {"eid": 102, "wht": 1, "et": "全职"},
        103: {"eid": 103, "wht": 2, "et": "实习"},
        104: {"eid": 104, "wht": 1, "et": "全职"},
        105: {"eid": 105, "wht": 1, "et": "全职"},
        106: {"eid": 106, "wht": 1, "et": "实习"},
        107: {"eid": 107, "wht": 2, "et": "实习"},
        108: {"eid": 108, "wht": 2, "et": "实习"},
        109: {"eid": 109, "wht": 1, "et": "全职"},
        110: {"eid": 110, "wht": 2, "et": "实习"},
        111: {"eid": 111, "wht": 1, "et": "全职"},
        112: {"eid": 112, "wht": 1, "et": "全职"},
        113: {"eid": 113, "wht": 1, "et": "全职"},
        114: {"eid": 114, "wht": 2, "et": "全职"},
        115: {"eid": 115, "wht": 1, "et": "全职"},

    }

    rule = "eid > 102 && wht = 1 and et != '实习'"
    f = Filter(rule)
    import time
    t = time.time()
    for i in range(100000):
        f.visit_res({"eid": 115, "wht": 1, "et": "全职"})
    print(time.time() - t)
    # 0.8s
    f = Filter("a + b * c")
    t = time.time()
    for i in range(100000):
        f.visit_res(a=1, b=2, c=4)
    print(time.time() - t)
    # 0.6s

    print(Filter("a and b and c").variables)
    # {'b', 'a', 'c'}



