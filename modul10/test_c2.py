from c2 import Dictionary

def test_empty_lookup():
    d = Dictionary()
    assert d.lookup_entry("x") is None
    assert d.size() == 0

def test_add_and_lookup():
    d = Dictionary()
    old = d.add_entry("dk", 10)
    assert old is None
    assert d.lookup_entry("dk") == 10
    assert d.size() == 1

def test_multiple_key_lengths():
    d = Dictionary()
    d.add_entry("", 1)
    d.add_entry("a", 2)
    d.add_entry("foo", 3)

    assert d.lookup_entry("") == 1
    assert d.lookup_entry("a") == 2
    assert d.lookup_entry("foo") == 3
    assert d.size() == 3

def test_replace_entry():
    d = Dictionary()
    d.add_entry("foo", 10)
    old = d.add_entry("foo", 20)

    assert old == 10
    assert d.lookup_entry("foo") == 20
    assert d.size() == 1  # replaced, not added

def test_delete():
    d = Dictionary()
    d.add_entry("abc", 5)

    val = d.delete_entry("abc")
    assert val == 5
    assert d.lookup_entry("abc") is None
    assert d.size() == 0

def test_contains_key():
    d = Dictionary()
    d.add_entry("hello", 99)

    assert d.contains_key("hello")
    assert not d.contains_key("world")
