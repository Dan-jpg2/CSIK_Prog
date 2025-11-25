from v3_5 import any_of

def test_any_of():
    assert any_of([True, True, True]) == True

def test_any_of1():
    assert any_of([True, False, True]) == True

def test_any_of2():
    assert any_of([False, False]) == False

def test_any_of_empty():
    assert any_of([]) == False

def test_any_of_AND():
    assert any_of([True, True]) == True
    assert any_of([True, False]) == True
    assert any_of([False, True]) == True
    assert any_of([False, False]) == False
    