from v2_6 import negate

def test_negate():
    v = [True, True, False, False]
    negate(v)
    assert v == [False, False, True, True]

def test_negate_empty():
    v = []
    negate(v)
    assert v == []
