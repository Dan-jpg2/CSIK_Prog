from v1_to_4 import every_second_char_of

def test_every_second_char_of():
    assert every_second_char_of('abcdefg')      == ['a', 'c', 'e', 'g']
    assert every_second_char_of('a')            == ['a']
    assert every_second_char_of('')             == []
    assert every_second_char_of('123456')       == ['1', '3', '5']

