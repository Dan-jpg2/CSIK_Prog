from v1_to_4 import *
from pytest import raises


def test_positives_of():
    assert positives_of([1,2,-2, 3,4,5,6, -1, -2]) == [1,2,3,4,5,6]

def test_positives_of_empty():
    assert positives_of([]) == []

def test_positives_of_negative():
    assert positives_of([-1, -2, -3]) == []

def test_non_empty_of():
    assert non_empty_of(["her", "er", "jeg"]) == ["her", "er", "jeg"]

def test_non_empty_of_empty():
    assert non_empty_of([]) == []

def test_non_empty_of_partial_empty():
    assert non_empty_of(["", "der", "", "er", "", "", "plads"]) == ["der", "er", "plads"]

def test_suspicious_login_attempts_of():
    assert suspicious_login_attempts_of(
        [('2025-10-30T07:25:14', 'root', False),
        ('2025-10-30T07:26:04', 'admin', False),
        ('2025-10-30T07:28:14', 'root', True)]
    ) == [('2025-10-30T07:25:14', 'root', False)]

def test_every_second_char_of():
    assert every_second_char_of("12345") == ["1", "3", "5"]

def test_every_second_char_of_empty():
    assert every_second_char_of("") == []

def test_remove_negatives_no_negative():
    v = [1, 2, 3, 4]
    remove_negatives(v)
    assert v == [1, 2, 3, 4]

def test_remove_negatives_only_negative():
    v = [-1, -2, -3, -4]
    remove_negatives(v)
    assert v == []

def test_remove_negatives_mixed():
    v = [1, -2, 3, -4, 5, -6]
    remove_negatives(v)
    assert v == [1, 3, 5]

def test_remove_empty_no_empty():
    v = ["hej", "med", "dig", "smukke"]
    remove_empty(v)
    assert v == ["hej", "med", "dig", "smukke"]

def test_remove_empty_empty():
    v = []
    remove_empty(v)
    assert v == []

def test_remove_empty_mixed():
    v = ["du", "", "kunne", "", "", "flyve"]
    remove_empty(v)
    assert v == ["du", "kunne", "flyve"]

def test_remove_every_other_normal():
    v = [1, 2, 3, 4, 5, 6]
    remove_every_other(v)
    assert v == [2, 4, 6]

def test_remove_every_other_empty():
    v = []
    remove_every_other(v)
    assert v == []

def test_remove_every_other_mixed():
    v = [2, "hej", 4, 5, "wup"]
    remove_every_other(v)
    assert v == ["hej", 5]

##### V2 afbildning opgaver #####

def test_doubled_positive():
    assert doubled([1, 2, 3, 4]) == [2, 4, 6, 8]

def test_doubled_negative():
    assert doubled([-1, -2, -3, -4]) == [-2, -4, -6, -8]

def test_doubled_mixed():
    assert doubled([1, -2, 3, -4, 0]) == [2, -4, 6, -8, 0]

def test_doubled_empty():
    assert doubled([]) == []

def test_squared_pos():
    assert squared([1,2,3,4]) == [1, 4, 9, 16]

def test_squared_neg():
    assert squared([-1,-2,-3,-4]) == [1, 4, 9, 16]

def test_squared_zero():
    assert squared([0]) == [0]

def test_squared_empt():
    assert squared([]) == []

def test_lengths_normal():
    assert lengths(['hej', 'smukke', 'hund']) == [3, 6, 4]

def test_lengths_empty():
    assert lengths([]) == []

def test_lengths_trick():
    assert lengths(['en', "", "snyder"]) == [2, 0, 6]

def test_decrement_pos():
    v = [1, 2, 3, 4]
    decrement(v)
    assert v == [0, 1, 2, 3]

def test_decrement_neg():
    v = [-1, -2, -3, -4]
    decrement(v)
    assert v == [-2, -3, -4, -5]

def test_decrement_empty():
    v = []
    decrement(v)
    assert v == []

def test_add_danish_vat_pos():
    v = [5, 87, 12500]
    add_danish_vat(v)
    assert v == [6.25, 108.75, 15625.0]

def test_add_danish_vat_empty():
    v = []
    add_danish_vat(v)
    assert v == []

def test_add_danish_vat_neg():
    v = [0, 100, -100]
    add_danish_vat(v)
    assert v == [0, 125, -125]

def test_negate_simple():
    v = [True, False, False, True]
    negate(v)
    assert v == [False, True, True, False]

def test_negate_empty():
    v = []
    negate(v)
    assert v == []

##### V3 reduktion opgaver #####

def test_sum_of_pos():
    assert sum_of([1, 2, 3, 4]) == 10

def test_sum_of_neg():
    assert sum_of([-1, -2, -3, -4]) == -10

def test_sum_of_empty():
    assert sum_of([]) == 0

def test_prod_of_pos():
    assert prod_of([1, 2, 3, 4]) == 24

def test_prod_of_neg():
    assert prod_of([-1, -2, -3, -4, -5]) == -120

def test_prod_of_empty():
    assert prod_of([]) == 1

def test_concat_of_simple():
    assert concat_of(["hej", "med", "dig"]) == "hejmeddig"

def test_concat_of_spaces():
    assert concat_of(["hej", " ", "din", " ", "superhelt"]) == "hej din superhelt"

def test_concat_of_empty():
    assert concat_of([""]) == ""

def test_all_of_simple():
    assert all_of([True, False]) == False

def test_all_of_empty():
    assert all_of([]) == True

def test_all_of_simple_long():
    assert all_of([False, True, True, True]) == False

def test_all_of_true():
    assert all_of([True, True]) == True

def test_any_of_true():
    assert any_of([False, False, False, True]) == True

def test_any_of_empty():
    assert any_of([]) == False

def test_any_of_false():
    assert any_of([False, False, False]) == False

## Test til modificeret all_of og any_of
def test_modified_all_of_simple():
    assert modified_all_of([True, False]) == False

def test_modified_all_of_empty():
    assert modified_all_of([]) == True

def test_modified_all_of_simple_long():
    assert modified_all_of([False, True, True, True]) == False

def test_modified_all_of_true():
    assert modified_all_of([True, True]) == True

def test_modified_any_of_true():
    assert modified_any_of([False, False, False, True]) == True

def test_modified_any_of_empty():
    assert modified_any_of([]) == False

def test_modified_any_of_false():
    assert modified_any_of([False, False, False]) == False
##################################################

def test_max_of_normal():
    assert max_of([2, -4, 3, 27, -1, 22]) == 27

def test_max_of_neg():
    assert max_of([-2, -44, -1, -22]) == -1

def test_max_of_empty():
    with raises(ValueError):
        assert max_of([])

def test_shortest_of_simple():
    v = ["hello", "du", "rimelig", "sjov"]
    assert shortest_of(v) == 'du'

def test_shortest_of_empty():
    with raises(ValueError):
        assert shortest_of([])

def test_avg_of_simple():
    v = [2, 4, 6, 3, 5]
    assert avg_of(v) == 4

def test_avg_of_empty():
    with raises(ValueError):
        assert avg_of([])

def test_avg_of_negative():
    v = [-2, -4, 2, -3]
    assert avg_of(v) == -1.75

def test_seperated_sum_of_simple():
    v = [1, -2, 3, -1, -2]
    assert seperated_sum_of(v) == (4, -5)

def test_seperated_sum_of_pos():
    v = [2, 4, 6, 8]
    assert seperated_sum_of(v) == (20, 0)

def test_seperated_sum_of_neg():
    v = [-5, -3, -10, -2]
    assert seperated_sum_of(v) == (0, -20)

def test_seperated_sum_of_empty():
    with raises(ValueError):
        v = []
        assert seperated_sum_of(v) == (0, 0)

##### V4 Kombinationer og indbyggede funktioner #####

def test_sum_squared_pos_of():
    assert sum_of(squared(positives_of([3, -2, 7, 1, -4]))) == 59

##### V4_2 ----- de 3 funktioner #####



def test_root_login_attempts_of():
    logs = [
        ("2025-10-30T07:25:14", "root", False),
        ("2025-10-30T07:26:04", "admin", True),
        ("2025-10-30T07:27:12", "root", True),
    ]
    assert root_login_attempts_of(logs) == [
        ("2025-10-30T07:25:14", "root", False),
        ("2025-10-30T07:27:12", "root", True),
    ]

def test_timestamps_of():
    logs = [
        ("2025-10-30T07:25:14", "root", False),
        ("2025-10-30T07:27:12", "root", True),
    ]
    assert timestamps_of(logs) == ["2025-10-30T07:25:14", "2025-10-30T07:27:12"]

def test_summary_of():
    logs = [
        ("2025-10-30T07:25:14", "root", False),
        ("2025-10-30T07:27:12", "root", True),
        ("2025-10-30T07:30:55", "root", False),
    ]
    assert summary_of(logs) == (
        "2025-10-30T07:25:14",  # first
        "2025-10-30T07:30:55",  # last
        2,                      # failures
        1                       # successes
    )

### V4_4 opgave
def test_1L_positives_of():
    assert positives_of_1L([1,2,-2, 3,4,5,6, -1, -2]) == [1,2,3,4,5,6]

def test_1L_positives_of_empty():
    assert positives_of_1L([]) == []

def test_1L_positives_of_negative():
    assert positives_of_1L([-1, -2, -3]) == []

def test_1L_doubled_positive():
    assert doubled_1L([1, 2, 3, 4]) == [2, 4, 6, 8]

def test_1L_doubled_negative():
    assert doubled_1L([-1, -2, -3, -4]) == [-2, -4, -6, -8]

def test_1L_doubled_mixed():
    assert doubled_1L([1, -2, 3, -4, 0]) == [2, -4, 6, -8, 0]

def test_1L_doubled_empty():
    assert doubled_1L([]) == []

def test_1L_sum_of_pos():
    assert sum_of_1L([1, 2, 3, 4]) == 10

def test_1L_sum_of_neg():
    assert sum_of_1L([-1, -2, -3, -4]) == -10

def test_1L_sum_of_empty():
    assert sum_of_1L([]) == 0