from v1_2 import non_empty_of

def test_non_empty_of():
    assert non_empty_of(["hej", "", "verden", "", "python"])    == ["hej", "verden", "python"]
    assert non_empty_of(["", "", ""])                           == []
    assert non_empty_of(["a", "b", ""])                         == ["a", "b"]
    assert non_empty_of([])                                     == []

