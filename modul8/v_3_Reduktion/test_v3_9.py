from v3_9 import avg_of
from pytest import raises

def test_avg_of_simple():
    v = [2, 4, 6, 3, 5]
    assert avg_of(v) == 4

def test_avg_of_empty():
    with raises(ValueError):
        assert avg_of([])

def test_avg_of_negative():
    v = [-2, -4, 2, -3]
    assert avg_of(v) == -1.75
