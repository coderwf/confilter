# -*- coding: utf-8 -*-
from cfilter.filter import Filter


class TestJoinFilter:
    def test_or(self):
        assert (Filter("0") | Filter("1")).visit_res() is True
        assert (Filter("1") | Filter("0")).visit_res() is True
        assert (Filter("0") | Filter("0")).visit_res() is False
        assert (Filter("1") | Filter("1")).visit_res() is True

        assert (Filter("0") | Filter("a")).visit_res(a=0) is False
        assert (Filter("1") | Filter("a")).visit_res(a=0) is True
        assert (Filter("a") | Filter("1")).visit_res(a=0) is True
        assert (Filter("a") | Filter("0")).visit_res(a=1) is True

        assert (Filter("a") | Filter("b")).visit_res(a=0, b=2) is True

    def test_and(self):
        assert (Filter("0") & Filter("1")).visit_res() is False
        assert (Filter("0") & Filter("0")).visit_res() is False
        assert (Filter("1") & Filter("1")).visit_res() is True
        assert (Filter("1") & Filter("0")).visit_res() is False

        assert (Filter("a") & Filter("0")).visit_res(a=1) is False
        assert (Filter("a") & Filter("1")).visit_res(a=1) is True
        assert (Filter("1") & Filter("a")).visit_res(a=0) is False
        assert (Filter("0") & Filter("a")).visit_res(a=0) is False
        assert (Filter("a") & Filter("b")).visit_res(a=1, b=2) is True
        assert (Filter("a") & Filter("b")).visit_res(a=1, b=0) is False

    def test_func(self):
        assert (Filter("1") + Filter("4")).visit_res() == 5
        assert (Filter("5") * Filter("4")).visit_res() == 20
        assert (Filter("1") / Filter("4")).visit_res() == 0.25
        assert (Filter("a") + Filter("4")).visit_res(a=8) == 12
        assert (Filter("2") * Filter("b")).visit_res(b=4) == 8

        assert (Filter("a") + Filter("b") + Filter("c")).visit_res(a=1, b=2, c=4) == 7

        assert (Filter("a + b") * Filter("c + d")).visit_res(a=1, b=2, c=3, d=4) == 21

