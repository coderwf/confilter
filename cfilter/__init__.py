# -*- coding: utf-8 -*-
"""
表达式计算解析器
支持:四则运算,pow(**),mod(%),and,not,or,xor,>,>=,<,<=,!=,==,=,表达式可以嵌套

samples:
使用visitor直接返回计算结果

Filter("name").visit_res({"name": "jack"}) // "jack"
Filter("age").visit_res({"age": 12})       // 12
Filter("add1").visit_res({"add1": 30})     // 30

Filter("0 and 0").visit_res() // False
Filter("1 and 0").visit_res() // False
Filter("1 and 1").visit_res() // True
Filter("0 && 0").visit_res() // False
Filter("1 or 1").visit_res() // True
Filter("1 or 0").visit_res() // True
Filter("1 || 0").visit_res() // True
Filter("not 1").visit_res() // False
Filter("not 0").visit_res() // True
Filter("! 0").visit_res() // True


Filter("3 > 2").visit_res() // True
Filter("3 <= 2").visit_res() // False
Filter("3 == 2").visit_res() // False
Filter("3 <= 2").visit_res() // False
Filter("3 > 3").visit_res() // False
Filter("3 > 2").visit_res() // True

# 支持变量
Filter("1 + 2 + 4 * 5").visit_res() // 23
Filter("3 * 5 + 4").visit_res() // 19
Filter("1 + 1.5 + 3 + (2 + 4)*2 + 4*3").visit_res() // 29.5
Filter("a + b * c +d").visit_res({"a": 1, "b": 3, "c": 3, "d": 4}) // 14

----------------------------------------------------------
#使用filter根据bool表达式过滤数据得到结果

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

rule_1 = "wht=1 && et='实习'"
res = Filter(rule_1).filter(data)
//output
{
    100: {"eid": 100, "wht": 1, "et": "实习"},
    106: {"eid": 106, "wht": 1, "et": "实习"},
}

-----------------------------------------------------------
rule_2 = "not (wht==1 && et=='实习')"
res = Filter(rule_2).filter(data)
//output
{
    101: {"eid": 101, "wht": 2, "et": "实习"},
    102: {"eid": 102, "wht": 1, "et": "全职"},
    103: {"eid": 103, "wht": 2, "et": "实习"},
    104: {"eid": 104, "wht": 1, "et": "全职"},
    105: {"eid": 105, "wht": 1, "et": "全职"},
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

"""