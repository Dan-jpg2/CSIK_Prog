from v3_10 import seperated_sum_of

def test_seperated_sum_of_simple():
    v = [1, -2, 3, -1, -2]
    assert seperated_sum_of(v) == (4, -5)

def test_seperated_sum_of_pos():
    v = [2, 4, 6, 8]
    assert seperated_sum_of(v) == (20, 0)

def test_seperated_sum_of_neg():
    v = [-5, -3, -10, -2]
    assert seperated_sum_of(v) == (0, -20)

def test_seperated_sum_of_empty():
    v = []
    assert seperated_sum_of(v) == (0, 0)