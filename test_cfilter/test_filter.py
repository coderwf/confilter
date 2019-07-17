# -*- coding: utf-8 -*-
import pytest
from cfilter.filter import Filter


class TestFilter:
    @staticmethod
    def cmp_list(l1, l2):
        if len(l1) != len(l2):
            return False
        l1 = set(l1)
        l2 = set(l2)
        for item in l1:
            if item not in l2:
                return False
        return True

    @pytest.fixture(scope="class")
    def data(self):
        # 1标准 2综合
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
        yield data_source

    def test_expression_1(self):
        rule = "a='综合工时' and b!='实习' "
        assert Filter(rule).visit_res({"a": "综合工时", "b": "实习"}) is False
        assert Filter(rule).visit_res({"a": "综合工时", "b": "全职"}) is True
        assert Filter(rule).visit_res({"a": "标准工时", "b": "实习"}) is False
        assert Filter(rule).visit_res({"a": "标准工时", "b": "全职"}) is False
        rule_1 = "not (a='综合工时' and b!='实习') "
        assert Filter(rule_1).visit_res({"a": "综合工时", "b": "实习"}) is True
        assert Filter(rule_1).visit_res({"a": "综合工时", "b": "全职"}) is False
        assert Filter(rule_1).visit_res({"a": "标准工时", "b": "实习"}) is True
        assert Filter(rule_1).visit_res({"a": "标准工时", "b": "全职"}) is True

    def text_expression_2(self, data):
        rule_1 = "wht==1 && et='实习'"
        res = Filter(rule_1).filter(data)
        assert self.cmp_list(list(res.items()), [100, 106])

        rule_2 = "not (wht==1 && et=='实习')"
        res = Filter(rule_2).filter(data)
        real_res = [num for num in range(100, 116)]
        real_res.remove(100)
        real_res.remove(106)
        assert self.cmp_list(list(res.items()), real_res)
