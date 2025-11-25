from v3_3 import concat_of

def test_concat_of_normal():
    v = ["hej", " ", "med"," ", "dig"," ", "smukke"]
    assert concat_of(v) == "hej med dig smukke"

def test_concat_of_empty():
    v = ["", "", ""]
    assert concat_of(v) == ""

def test_concat_of_empty2():
    v = []
    assert concat_of(v) == ""