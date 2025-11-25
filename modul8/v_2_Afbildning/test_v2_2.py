from v2_2 import squared

def test_squared():
    v = [2, 3, 4, 5]
    assert squared(v) == [4, 9, 16, 25]

def test_squared1():
    v = [0, 1, -1]
    assert squared(v) == [0, 1, 1]

def test_squared2(): 
    v = []
    assert squared(v) == []
    