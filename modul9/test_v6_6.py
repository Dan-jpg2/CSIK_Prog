from v6_6 import combined_sales_of

def test_combined_sales_of():
    a = [('apple', 10), ('banana', 5), ('pear', 8)]
    b = [('banana', 7), ('cherry', 3), ('pear', 2)]
    assert combined_sales_of(a, b) == [
        ('apple', 10), ('banana', 12), ('cherry', 3), ('pear', 10)
    ]