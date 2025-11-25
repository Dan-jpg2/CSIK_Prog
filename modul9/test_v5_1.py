from v5_1 import cum_sum_of

def test_cum_sum_of():
    assert cum_sum_of([1,2,3,4]) == [1,3,6,10]
    assert cum_sum_of([5]) == [5]
    assert cum_sum_of([]) == []
    assert cum_sum_of([2, -3, 4, 7]) == [2, -1, 3, 10]
    
