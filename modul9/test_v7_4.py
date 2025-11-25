from v7_4 import partial_sort


def test_partial_sort():
    values = [4, 1, 4, 3, 2, 8, 7, 7, 1]
    w, b = partial_sort(4, values)
    assert values == [1, 3, 2, 1, 4, 4, 8, 7, 7]
    assert (w, b) == (4, 6)

    