from v2_3 import lengths

def test_lengths():
    v = ["dette", "er", "en", "", "snyder"]
    assert lengths(v) == [5, 2, 2, 0, 6]

def test_lengths1():
    v = []
    assert lengths(v) == []

def test_lengths2():
    v = [""]
    assert lengths(v) == [0]


