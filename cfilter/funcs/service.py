# -*- coding: utf-8 -*-
from cfilter.funcs.builtin import builtin_funcs


class FuncService:

    funcs_map = {}
    funcs_map.update(builtin_funcs)

    @staticmethod
    def register(name, func):
        FuncService.funcs_map[name.lower()] = func

    @staticmethod
    def exists(name):
        return name in FuncService.funcs_map

    @staticmethod
    def unregister(name):
        FuncService.funcs_map.pop(name, None)

    @staticmethod
    def exec(name, *args, **kwargs):
        func = FuncService.funcs_map.get(name.lower())
        if func is None:
            raise Exception("func %s not found" % name)

        return func(*args, **kwargs)


# 自定义函数
def customer_func(name):
    def _func(func):
        FuncService.register(name, func)
        return func
    return _func




