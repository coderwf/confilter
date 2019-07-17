# -*- coding: utf-8 -*-
from antlr4.error.ErrorListener import ErrorListener


class FilterSyntaxError(Exception):
    def __init__(self, line, column, msg):
        self.msg = "line:%s, column:%s with %s" % (line, column, msg)


class FilterErrorListener(ErrorListener):
    INSTANCE = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise FilterSyntaxError(line, column, msg)


FilterErrorListener.INSTANCE = FilterErrorListener()