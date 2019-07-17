# -*- coding: utf-8 -*-
import antlr4
from cfilter.fantlr.CFilterLexer import CFilterLexer
from cfilter.fantlr.CFilterParser import CFilterParser
from cfilter.visitor.myvisitor import MyVisitor
from cfilter.visitor.elistener import FilterErrorListener


class Filter:
    def __init__(self, rule):
        stream = antlr4.InputStream(rule)
        fl = CFilterLexer(stream)
        fl.removeErrorListeners()
        fl.addErrorListener(FilterErrorListener.INSTANCE)
        token_stream = antlr4.CommonTokenStream(fl)
        tree = CFilterParser(token_stream)

        tree.removeErrorListeners()
        tree.addErrorListener(FilterErrorListener.INSTANCE)
        self.visitor = MyVisitor()
        self.tree = tree

    def visit_res(self, data=None):
        self.tree.reset()
        return self.visitor.visit_res(self.tree.cfilter(), data_source=data)

    def _filter_dict(self, data_source):
        new_data_source = dict()
        for employee_id, data in data_source.items():
            self.tree.reset()
            ok = bool(self.visit_res(data))
            if ok:
                new_data_source[employee_id] = data

        return new_data_source

    def _filter_list(self, data_source):
        new_data_source = []
        for data in data_source:
            self.tree.reset()
            ok = bool(self.visit_res(data))
            if ok:
                new_data_source.append(data)
        return new_data_source

    def filter(self, data_source):
        if not isinstance(data_source, (list, tuple, dict)):
            raise Exception("data_source must be (list, tuple, dict)")

        if isinstance(data_source, dict):
            return self._filter_dict(data_source)
        return self._filter_list(data_source)


if __name__ == "__main__":
    rule_1 = "not (a='综合工时' and b!='实习') "
    Filter(rule_1).visit_res({"a": "综合工时", "b": "实习"})
    print(Filter("1 or 1 and 0").visit_res())