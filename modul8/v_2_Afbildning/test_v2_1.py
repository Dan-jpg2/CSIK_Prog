from v2_1 import doubled

def test_doubled():
    v = [2, -2, 3, 5, 0]
    assert doubled(v) == [4, -4, 6, 10, 0]

def test_doubled1():
    v = []
    doubled(v)
    assert v == []

def test_doubled2():
    v = [1, -100, 0, -1]
    assert doubled(v) == [2, -200, 0, -2]