from c1_dictionary import *

def test_empty_lookup():
    d = Dictionary()
    assert d.lookup_entry("x") is None
    assert d.size() == 0

def test_add_and_lookup():
    d = Dictionary()
    old = d.add_entry("dk", "Copenhagen")

    assert old is None
    assert d.lookup_entry("dk") == "Copenhagen"
    assert d.size() == 1

def test_replace_entry():
    d = Dictionary()
    d.add_entry("dk", "Copenhagen")

    old = d.add_entry("dk", "New City")

    assert old == "Copenhagen"
    assert d.lookup_entry("dk") == "New City"
    assert d.size() == 1  # size unchanged

def test_contains():
    d = Dictionary()
    d.add_entry("a", 1)
    assert d.contains_key("a") is True
    assert d.contains_key("b") is False

def test_delete():
    d = Dictionary()
    d.add_entry("x", 123)
    
    val = d.delete_entry("x")
    assert val == 123
    assert d.lookup_entry("x") is None
    assert d.size() == 0

def test_delete_missing():
    d = Dictionary()
    assert d.delete_entry("none") is None
