from i4 import negatives_of

def test_negatives_of_empty():
    assert negatives_of([]) == 0

def test_negatives_of_single_negative():
    assert negatives_of(['-1']) == 1

def test_negatives_of_single_zero():
    assert negatives_of(['0']) == 0

def test_negatives_of_two_negatives():
    assert negatives_of(['-1', '-7']) == 2

def test_negatives_of_three_mixed():
    assert negatives_of(['-1', '0', '-7']) == 2

def test_negatives_of_stream():
    import io
    assert negatives_of(io.StringIO('-1\n0\n-7')) == 2