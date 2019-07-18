# -*- coding: utf-8 -*-


class FilterError(Exception):
    pass


class FilterSyntaxError(FilterError):
    def __init__(self, line, column, msg):
        self.message = "line:%s, column:%s with %s" % (line, column, msg)


class FuncNotFound(FilterError):
    def __init__(self, func_name):
        self.message = "func [%s] not found" % func_name


class IdentifierNotFound(FilterError):
    def __init__(self, identifier):
        self.message = "identifier [%s] not found" % identifier
