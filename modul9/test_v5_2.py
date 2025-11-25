from v5_2 import cum_max_of, cum_max_of_1L

def test_cum_max_of():
    assert cum_max_of([2, -3, 4, 8, 7]) == [2, 2, 4, 8, 8]
    assert cum_max_of([]) == []
    assert cum_max_of([1]) == [1]

def test_cum_max_of1L():
    assert cum_max_of([2, -3, 4, 8, 7]) == [2, 2, 4, 8, 8]
    assert cum_max_of([]) == []
    assert cum_max_of([1]) == [1]