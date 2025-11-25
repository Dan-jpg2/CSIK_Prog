from v1_6 import remove_empty

def test_remove_empty():
    v = ['1', '2', '3', '4']
    remove_empty(v)
    assert v == ['1', '2', '3', '4']

def test_remove_empty1():
    v = ['a', '', 'b', 'c']
    remove_empty(v)
    assert v == ['a', 'b', 'c']

def test_remove_empty2():
    v = ["", "", ""]
    remove_empty(v)
    assert v == []

def test_remove_empty3():
    v = ['test', '', 'Af', '', 'hjul']
    remove_empty(v)
    assert v == ['test', 'Af', 'hjul']
    