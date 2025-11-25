from v3_8 import shortest_of
from pytest import raises

def test_shortest_of_simple():
    v = ["hello", "du", "rimelig", "sjov"]
    assert shortest_of(v) == 'du'

def test_shortest_of_empty():
    with raises(ValueError):
        assert shortest_of([])

    