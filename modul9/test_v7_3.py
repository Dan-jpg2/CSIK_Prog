from v7_3 import merge_sort_of

def test_merge_sort_of():
    assert merge_sort_of([4, 1, 7, 3]) == [1, 3, 4, 7]
    assert merge_sort_of([]) == []

    