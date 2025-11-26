from c3 import Dictionary

import pytest


def test_simple_put_get():
    d = Dictionary()
    d.put("a", 1)
    d.put("b", 2)
    d.put("c", 3)
    
    assert d.get("a") == 1
    assert d.get("b") == 2
    assert d.get("c") == 3
    assert len(d) == 3

def test_overwrite_value():
    d = Dictionary()
    d.put("a", 1)
    d.put("a", 100)
    
    assert d.get("a") == 100
    assert len(d) == 1

def test_remove_and_keyerror():
    d = Dictionary()
    d.put("a", 1)
    d.put("b", 2)
    
    d.remove("a")
    assert len(d) == 1
    with pytest.raises(KeyError):
        d.get("a")

def test_key_types():
    d = Dictionary()
    d.put(42, "number")
    d.put((1, "x"), "tuple")
    
    assert d.get(42) == "number"
    assert d.get((1, "x")) == "tuple"

def test_timestamps():
    d = Dictionary()
    timestamps = [f"2025-11-18T22:0{i}:00" for i in range(5)]
    for i, ts in enumerate(timestamps):
        d.put(ts, i)
    
    for i, ts in enumerate(timestamps):
        assert d.get(ts) == i

def test_auto_resize():
    d = Dictionary()
    initial_capacity = len(d._v)
    for i in range(20):
        d.put(f"key{i}", i)
    assert len(d._v) > initial_capacity

def test_auto_shrink():
    d = Dictionary()
    for i in range(20):
        d.put(f"key{i}", i)
    capacity_after_growth = len(d._v)
    
    for i in range(20):
        d.remove(f"key{i}")
    assert len(d._v) <= capacity_after_growth
