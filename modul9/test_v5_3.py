from v5_3 import cum_union_of, cum_union_of_1L

def test_cum_union_of():
    assert cum_union_of([{2, 3}, {2, 4}, {3}, {3, 6}]) == [
        {2, 3},
        {2, 3, 4},
        {2, 3, 4},
        {2, 3, 4, 6},
    ]

def test_cum_union_of_1L():
    assert cum_union_of([{2, 3}, {2, 4}, {3}, {3, 6}]) == [
        {2, 3},
        {2, 3, 4},
        {2, 3, 4},
        {2, 3, 4, 6},
    ]