from v3_4 import all_of

def test_all_of():
    assert all_of([True, True, True]) == True

def test_all_of1():
    assert all_of([True, False, True]) == False

def test_all_of2():
    assert all_of([False, False]) == False

def test_all_of_empty():
    assert all_of([]) == True

def test_all_of_AND():
    assert all_of([True, True]) == True
    assert all_of([True, False]) == False
    assert all_of([False, True]) == False
    assert all_of([False, False]) == False
    