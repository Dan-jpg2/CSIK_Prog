from v6_5 import merge_of

def test_merge_of():
    assert merge_of([2, 5, 9], [1, 3, 5, 11]) == [1, 2, 3, 5, 5, 9, 11]