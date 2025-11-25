from v2_4 import decrement

def test_decrement():
    v = [2, -3, 4, 0, 1]
    decrement(v)
    assert v == [1, -4, 3, -1, 0]

def test_decrement1():
    v = []
    decrement(v)
    assert v == []

