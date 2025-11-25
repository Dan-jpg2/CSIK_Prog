from v3_7 import max_of
from pytest import raises

def test_max_of_simple():
    v = [1, 3, -2, 23]
    assert max_of(v) == 23

def test_max_of_negative():
    v = [-1, -4, -74, -2]
    assert max_of(v) == -1

def test_max_of_empty():
    with raises(ValueError):
        assert max_of([])


