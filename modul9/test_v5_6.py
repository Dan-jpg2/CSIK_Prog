from v5_6 import moving_avg_of

def test_moving_avg_of():
    assert moving_avg_of([2, -3, 4, 8, 6]) == [2, -0.5, 1, 3, 6]