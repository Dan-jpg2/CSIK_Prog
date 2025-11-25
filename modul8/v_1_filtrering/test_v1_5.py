from v1_5 import remove_negatives

def test_remove_negatives():
    v = [3, -2, 7, 1, -4]
    remove_negatives(v)
    assert v == [3, 7, 1]

def test_remove_negatives1():
    v = [1, 5, 7, 9, 10]
    remove_negatives(v)
    assert v == [1, 5, 7, 9, 10]

def test_remove_negatives2():
    v = [-1, -5, -7, -9]
    remove_negatives(v)
    assert v == []

