# -*- coding: utf-8 -*-

builtin_funcs = {
    "+": lambda *x: x[0] if len(x) == 1 else x[0] + x[1],
    "add": lambda x, y: x + y,
    "-": lambda *x: x[0] if len(x) == 1 else x[0] - x[1],
    "sub": lambda x, y: x - y,
    "mul": lambda x, y: x * y,
    "*": lambda x, y: x * y,
    "div": lambda x, y: x / y,
    "/": lambda x, y: x / y,
    "**": lambda x, y: x ** y,
    "pow": lambda x, y: x ** y,

    "round": lambda x, y: round(x, y),
    "mod": lambda x, y: x % y,
    "%": lambda x, y: x % y,

    "and": lambda x, y: bool(x and y),
    "&&": lambda x, y: bool(x and y),

    "or": lambda x, y: bool(x or y),
    "||": lambda x, y: bool(x or y),

    "xor": lambda x, y: bool(x) != bool(y),
    "^|": lambda x, y: bool(x) != bool(y),

    "not": lambda x: not x,
    "!": lambda x: not x,
    "~": lambda x: ~x,

    ">": lambda x, y: x > y,
    "<": lambda x, y: x < y,
    ">=": lambda x, y: x >= y,
    "<=": lambda x, y: x <= y,
    "=": lambda x, y: x == y,

    "==": lambda x, y: x == y,
    "is": lambda x, y: x is y,
    "isn't": lambda x, y: x is not y,
    "is_not": lambda x, y: x is not y,
    "!=": lambda x, y: x != y,

    "int": lambda x: int(x),
    "float": lambda x: float(x),
    "str": lambda x: str(x),

}
