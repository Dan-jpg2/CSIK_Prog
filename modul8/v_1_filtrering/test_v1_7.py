from v1_7 import remove_every_other

def test_remove_every_other():
    v = [1, 2, 3, 4, 5]
    remove_every_other(v)
    assert v == [2, 4]

def test_remove_every_other1():
    v = ['hej', 'med', 'dig']
    remove_every_other(v)
    assert v == ['med']

def test_remove_every_other2():
    v = ['enlig']
    remove_every_other(v)
    assert v == []

def test_remove_every_other3():
    v = [1, None, 'cookie']
    remove_every_other(v)
    assert v == [None]

def test_remove_every_other4():
    v = []
    remove_every_other(v)
    assert v == []