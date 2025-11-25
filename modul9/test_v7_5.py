from v7_5 import quick_sort


def test_quick_sort():
    values = [4, 1, 4, 3, 2, 8, 7, 7, 1]
    quick_sort(values)
    assert values == sorted([4, 1, 4, 3, 2, 8, 7, 7, 1])
    