from calc import sum

def test_sum_positive():
    assert sum(2, 3) == 5

def test_sum_negative():
    assert sum(-1, -1) == -2

def test_sum_mixed():
    assert sum(-1, 1) == 0

def test_sum_float():
    assert sum(1.2, 1.5) == 2.7

def test_sum_float():
    assert sum(1.2, -1.2) == 0