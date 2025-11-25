from v2_5 import add_danish_vat

def test_add_danish_vat():
    v = [0, 100, -100]
    add_danish_vat(v)
    assert v == [0, 125, -125]

def test_add_danish_vat1():
    v = []
    add_danish_vat(v)
    assert v == []

def test_add_danish_vat2():
    v = [5, 87, 12500]
    add_danish_vat(v)
    assert v == [6.25, 108.75, 15625.0]
    
