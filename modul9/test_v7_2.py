from v7_2 import shuffle

def test_shuffle():
    values = [10, 2, 30, 4, 50]
    shuffle(values)
    assert sorted(values) == [2, 4, 10, 30, 50]  

