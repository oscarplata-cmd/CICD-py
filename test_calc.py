import pytest
from calc import Calculadora

def test_sum_positive():
    c = Calculadora()
    assert c.sum(2, 3) == 5

def test_sum_negative():
    c = Calculadora()
    assert c.sum(-1, -1) == -2

def test_mul():
    c = Calculadora()
    assert c.mul(-1, 1) == -1

def test_mul_negative():
    c = Calculadora()
    assert c.mul(1.2, 1.5) ==  pytest.approx(1.8)
