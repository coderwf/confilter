# -*- coding: utf-8 -*-
import antlr4
from cfilter.fantlr.CFLexer import CFLexer
from cfilter.fantlr.CFilter import CFilter
from cfilter.visitor.myvisitor import MyVisitor
from cfilter.visitor.elistener import FilterErrorListener


class Filter:
    def __init__(self, rule):
        self.rule = rule
        self.identifiers = None
        self.node = None
        self._parse()

    def _parse(self):
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

    @property
    def variables(self):
        return self.identifiers

    # 如果结果是个常量则需要直接返回结果
    def visit_res(self, value_map=None, **kwargs):
        if self.identifiers is None or len(self.identifiers) == 0:
            self.node = self.node.visit()
            self.__dict__["visit_res"] = self.visit_const_res
            return self.node
        return self.node.visit(value_map, **kwargs)

    def visit_const_res(self, *args):
        return self.node

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
