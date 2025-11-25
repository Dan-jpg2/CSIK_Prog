from v3_2 import prod_of

def test_prod_of_normal():
    v = [1, 2, 3, 4]
    assert prod_of(v) == 24

def test_prod_of_negative():
    v = [-2, 3, -4, -10]
    assert prod_of(v) == -240

def test_prod_of_empty():
    v =[]
    assert prod_of(v) == 1