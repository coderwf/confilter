# -*- coding: utf-8 -*-

# 将表达式分解为nodes构成的树
from abc import abstractmethod
from cfilter.visitor.errors import IdentifierNotFound, FuncNotFound
from cfilter.funcs.service import FuncService


class Node:
    @abstractmethod
    def visit(self, *args, **kwargs):
        pass


class Const(Node):
    __slots__ = ["value"]

    def __init__(self, value):
        self.value = value

    def visit(self, *args, **kwargs):
        return self.value


class Consts(Node):
    __slots__ = ["values"]

    def __init__(self, values):
        self.values = values

    def visit(self, *args, **kwargs):
        return self.values


class Exps(Node):
    __slots__ = ["exps"]

    def __init__(self, exps):
        self.exps = exps

    def visit(self, value_map, **kwargs):
        return tuple(exp.visit(value_map, **kwargs) for exp in self.exps)


class Identifier(Node):
    __slots__ = ["identifier"]

    def __init__(self, identifier):
        self.identifier = identifier

    # 从value_map或者kwargs中取
    def visit(self, value_map, **kwargs):
        val = value_map.get(self.identifier) if value_map else None
        if val is None:
            val = kwargs.get(self.identifier)
        if val is None:
            raise IdentifierNotFound(self.identifier)
        return val


class Func(Node):
    __slots__ = ["func", "args"]

    def __init__(self, func, *args):
        self.func = func
        # 对于只有一个参数
        self.args = args

    def visit(self, value_map, **kwargs):
        visit_args = tuple(arg.visit(value_map, **kwargs) for arg in self.args)
        if not FuncService.exists(self.func):
            raise FuncNotFound(self.func)
        return FuncService.exec(self.func, *visit_args)


# 可以优化计算逻辑
class AndFunc(Func):
    __slots__ = ["args"]

    def __init__(self, *args, func="and"):
        Func.__init__(self, func, *args)

    def visit(self, value_map, **kwargs):
        left_val = self.args[0].visit(value_map, **kwargs)
        if bool(left_val) is False:
            return False
        right_val = self.args[1].visit(value_map, **kwargs)
        return bool(right_val)


class OrFunc(Func):
    __slots__ = ["args"]

    def __init__(self, *args, func="or"):
        Func.__init__(self, func, *args)

    def visit(self, value_map, **kwargs):
        left_val = self.args[0].visit(value_map, **kwargs)
        if bool(left_val) is True:
            return True
        right_val = self.args[1].visit(value_map, **kwargs)
        return bool(right_val)
