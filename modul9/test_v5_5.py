from v5_5 import cum_avg_of

def test_cum_avg_of():
    assert cum_avg_of([2, -3, 4, 8, 7]) == [2, -0.5, 1, 2.75, 3.6]
    assert cum_avg_of([]) == []