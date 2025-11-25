from v1_1 import positives_of

#test
def test_positives_of():
    assert positives_of([3, -2, 7, 1, -4])      == [3, 7, 1]
    assert positives_of([-5, -2, -9])           == []
    assert positives_of([0, 2, 5])              == [2, 5]
    assert positives_of([])                     == []
