from v6_1 import vector_sum_of, vector_sum_of_1L

def test_vector_sum_of():
    assert vector_sum_of([10, 40, 20], [5, 25, 8]) == [15, 65, 28]
    assert vector_sum_of([-10, -40, -20], [5, 25, 8]) == [-5, -15, -12]

    assert vector_sum_of([], []) == []


def test_vector_sum_of_1L():
    assert vector_sum_of([10, 40, 20], [5, 25, 8]) == [15, 65, 28]
    assert vector_sum_of([-10, -40, -20], [5, 25, 8]) == [-5, -15, -12]
    assert vector_sum_of([], []) == []