from v6_2 import vector_min_of_1L

def test_vector_min_of():
    assert vector_min_of_1L([5, 40, 20], [10, 25, 8]) == [5, 25, 8]
    assert vector_min_of_1L([-5, 40, 20], [10, 25, 8]) == [-5, 25, 8]

def test_vector_min_of_1L():
    assert vector_min_of_1L([5, 40, 20], [10, 25, 8]) == [5, 25, 8]
    assert vector_min_of_1L([-5, 40, 20], [10, 25, 8]) == [-5, 25, 8]