from v3_1 import sum_of

def test_sum_of_simple():
    assert sum_of([1, 2, 3, 4]) == 10

def test_sum_of_negatives():
    v = [-1, -2, -3, -4]
    assert sum_of(v) == -10

def test_sum_of_mixed():
    v = [-5, 2, 3, -1, 2]
    assert sum_of(v) == 1

def test_sum_of_none():
    v = []
    assert sum_of(v) == 0
