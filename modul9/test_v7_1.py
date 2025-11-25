from v7_1 import reverse, reverse_of

def test_reverse_of():
    assert reverse_of([1, 2, 3]) == [3, 2, 1]
    assert reverse_of([]) == []


def test_reverse():
    values = [1, 2, 3, 4]
    reverse(values)
    assert values == [4, 3, 2, 1]

