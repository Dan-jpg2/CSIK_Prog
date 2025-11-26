import o5_dictionary


def test_lookup_in_empty():
    d = o5_dictionary.create()
    assert o5_dictionary.lookup_entry(d, 'unknown') is None


def test_add_to_empty():
    d = o5_dictionary.create()
    old_value = o5_dictionary.set_entry(d, 'dk', 'Copenhagen')
    assert old_value is None
    assert o5_dictionary.lookup_entry(d, 'dk') == 'Copenhagen'
    assert o5_dictionary.lookup_entry(d, 'unknown') is None


def test_update_existing_entry():
    d = o5_dictionary.create()
    o5_dictionary.set_entry(d, 'us', 'Washington')
    old_value = o5_dictionary.set_entry(d, 'us', 'New York')
    assert old_value == 'Washington'
    assert o5_dictionary.lookup_entry(d, 'us') == 'New York'


def test_delete_entry():
    d = o5_dictionary.create()
    o5_dictionary.set_entry(d, 'fr', 'Paris')
    old_value = o5_dictionary.delete_entry(d, 'fr')
    assert old_value == 'Paris'
    assert o5_dictionary.lookup_entry(d, 'fr') is None


def test_clear_and_keys():
    d = o5_dictionary.create()
    o5_dictionary.set_entry(d, 'dk', 'Copenhagen')
    o5_dictionary.set_entry(d, 'se', 'Stockholm')
    assert sorted(o5_dictionary.keys(d)) == ['dk', 'se']
    o5_dictionary.clear(d)
    assert o5_dictionary.keys(d) == []
    assert o5_dictionary.lookup_entry(d, 'dk') is None
