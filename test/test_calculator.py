# -*- coding: utf8 -*-

import pytest
from calculator import calculator


def test_1():
    answer = calculator('2+2')
    assert answer == 4.0


def test_2():
    answer = calculator('-2+2')
    assert answer == 0.0


def test_3():
    answer = calculator('15/(7-(1+1))*3-(2+(1+1))')
    assert answer == 5.0


def test_4():
    answer = calculator('15/(7-(1+1))*3-(-2+(1+1))')
    assert answer == 9.0


def test_5():
    answer = calculator('15/(7-(1+1))*3-(2+(1+1))*15/(7-(1+1))*'
                        '3-(2+(1+1))*(15/(7-(1+1))*3-(2+(1+1))+15/'
                        '(7-(1+1))*3-(2+(1+1)))')
    assert answer == -67.0


def test_6():
    answer = calculator('-15/(7-(1+1))*3-(2+(1+1))*15/(7-(1+1))*'
                        '3-(2+(1+1))*(15/(7-(1+1))*3-(2+(1+1))+15/'
                        '(7-(1+1))*3-(2+(1+1)))')
    assert answer == -85.0


def test_7():
    answer = calculator('3^4')
    assert answer == 81.0


def test_8():
    with pytest.raises(ZeroDivisionError):
        answer = calculator('2/0')
