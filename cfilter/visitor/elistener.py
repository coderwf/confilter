# -*- coding: utf-8 -*-
from antlr4.error.ErrorListener import ErrorListener
from cfilter.visitor.errors import FilterSyntaxError


class FilterErrorListener(ErrorListener):
    INSTANCE = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise FilterSyntaxError(line, column, msg)


FilterErrorListener.INSTANCE = FilterErrorListener()