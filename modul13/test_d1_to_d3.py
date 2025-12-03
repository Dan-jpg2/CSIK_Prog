from d1_to_3 import *

# Opgave d1_1
def test_in_december_skips_other_months():
    logs = [('pc-001', '2025-11-30T23:59:59', 'root', 'failure')]
    assert list(in_december(logs)) == []
def test_in_december_keeps_december_entries():
    logs = [('pc-001', '2025-12-30T23:59:59', 'root', 'failure')]
    assert list(in_december(logs)) == logs
def test_in_december_is_streaming():
    log1 = ('pc-001', '2025-11-30T23:59:59', 'root', 'success')
    log2 = ('pc-002', '2025-12-01T00:00:00', 'root', 'failure')
    log3 = ('pc-003', '2025-12-02T12:00:00', 'leaf', 'failure')
    logs = iter([log1, log2, log3])

    filtered = in_december(logs)
    assert next(filtered) == log2
    assert next(filtered) == log3
    assert list(filtered) == []    
    
# Opgave d1_2    
def test_in_date_range_skips_before_start():
    logs = [('pc-001', '2025-11-01T00:00:00', 'root', 'failure')]
    assert list(in_date_range(logs, '2025-11-02', '2025-11-30')) == []
def test_in_date_range_skips_after_end():
    logs = [('pc-002', '2025-12-31T23:59:59', 'leaf', 'success')]
    assert list(in_date_range(logs, '2025-11-01', '2025-12-01')) == []
def test_in_date_range_includes_bounds():
    logs = [
        ('pc-003', '2025-11-01T12:00:00', 'root', 'failure'),
        ('pc-004', '2025-11-15T08:00:00', 'leaf', 'success'),
        ('pc-005', '2025-11-30T23:59:59', 'root', 'failure'),
    ]
    assert list(in_date_range(logs, '2025-11-01', '2025-11-30')) == logs
def test_in_date_range_is_streaming():
    log1 = ('pc-006', '2025-10-31T23:59:59', 'root', 'success')
    log2 = ('pc-007', '2025-11-01T00:00:00', 'root', 'failure')
    log3 = ('pc-008', '2025-11-15T00:00:00', 'leaf', 'failure')
    log4 = ('pc-009', '2025-12-01T00:00:00', 'root', 'failure')
    logs = iter([log1, log2, log3, log4])

    filtered = in_date_range(logs, '2025-11-01', '2025-11-30')

    assert next(filtered) == log2
    assert next(filtered) == log3
    assert list(filtered) == []

# Opgave d1_3
def test_on_host_filters_correctly():
    sample = [
        ("host1", "t1", "u1", False),
        ("host2", "t2", "u2", True),
        ("host1", "t3", "u3", False),
    ]
    result = list(on_host(sample, "host1"))
    assert result == [
        ("host1", "t1", "u1", False),
        ("host1", "t3", "u3", False),
    ]

# Opgave d1_4
def test_by_user_skips_other_users():
    logs = [
        ("pc-001", "t1", "alice", False)
    ]
    assert list(by_user(logs, "bob")) == []
def test_by_user_keeps_matching_user():
    logs = [
        ("pc-002", "t2", "bob", True)
    ]
    assert list(by_user(logs, "bob")) == logs
def test_by_user_is_streaming():
    log1 = ("pc-003", "t3", "root", False)
    log2 = ("pc-004", "t4", "bob", True)
    log3 = ("pc-005", "t5", "alice", False)

    logs = iter([log1, log2, log3])
    filtered = by_user(logs, "bob")

    assert next(filtered) == log2
    assert list(filtered) == []

# Opgave 2 her fra

#Opgave d2_1
def test_as_dicts_transforms_correctly():
    logs = [
        ("pluto","2024-01-01T00:04:34","gefu","success")
    ]
    expected = [
        {'hostname':'pluto','timestamp':'2024-01-01T00:04:34','username':'gefu','result':'success'}
    ]
    assert list(as_dicts(logs)) == expected
def test_as_dicts_is_streaming():
    logs = iter([
        ("pluto","2024-01-01T00:04:34","gefu","success"),
        ("pc-029","2024-01-01T00:10:17","ereg","success")
    ])
    stream = as_dicts(logs)
    assert next(stream) == {'hostname':'pluto','timestamp':'2024-01-01T00:04:34','username':'gefu','result':'success'}
    assert next(stream) == {'hostname':'pc-029','timestamp':'2024-01-01T00:10:17','username':'ereg','result':'success'}
    assert list(stream) == []

#Opgave d2_2
def test_with_boolean_results():
    logs = [
        {'hostname':'pluto','timestamp':'2024-01-01T00:04:34','username':'gefu','result':'success'},
        {'hostname':'pc-029','timestamp':'2024-01-01T00:10:17','username':'ereg','result':'failure'}
    ]
    expected = [
        {'hostname':'pluto','timestamp':'2024-01-01T00:04:34','username':'gefu','result':True},
        {'hostname':'pc-029','timestamp':'2024-01-01T00:10:17','username':'ereg','result':False}
    ]
    assert list(with_boolean_results(logs)) == expected

#Opgave d2_3
def test_with_dates():
    logs = [
        {'hostname':'pluto','timestamp':'2024-01-01T00:04:34','username':'gefu','result':'success'}
    ]
    expected = [
        {'hostname':'pluto','timestamp':'2024-01-01','username':'gefu','result':'success'}
    ]
    assert list(with_dates(logs)) == expected

#Opgave d2_4
def test_with_risk_scores_all_cases():
    # Opsæt employees og hosts
    employees = [
        (0, 'Alice', 'alice_id', 'sales'),
        (1, 'Bob', 'bob_id', 'engineering')
    ]
    employees_index = {e[1]: i for i, e in enumerate(employees)}

    hosts = [
        (0, 'pc-001', 'sales'),
        (1, 'pc-002', 'engineering'),
        (2, 'pc-003', 'finance')
    ]
    hosts_index = {h[1]: i for i, h in enumerate(hosts)}

    # Testdatastrøm
    logs = [
        # Green: kendt bruger, kendt host, samme afdeling
        {'hostname': 'pc-001', 'timestamp': '2024-01-01', 'username': 'Alice', 'result': True},

        # Yellow: kendt bruger, kendt host, forskellig afdeling, failure
        {'hostname': 'pc-002', 'timestamp': '2024-01-01', 'username': 'Alice', 'result': False},

        # Red: kendt bruger, kendt host, forskellig afdeling, success
        {'hostname': 'pc-002', 'timestamp': '2024-01-01', 'username': 'Alice', 'result': True},

        # Red: kendt bruger, ukendt host, failure
        {'hostname': 'pc-999', 'timestamp': '2024-01-01', 'username': 'Bob', 'result': False},

        # Critical: kendt bruger, ukendt host, success
        {'hostname': 'pc-999', 'timestamp': '2024-01-01', 'username': 'Bob', 'result': True},

        # Critical: ukendt bruger, success
        {'hostname': 'pc-003', 'timestamp': '2024-01-01', 'username': 'Charlie', 'result': True},

        # Red: ukendt bruger, failure
        {'hostname': 'pc-003', 'timestamp': '2024-01-01', 'username': 'Charlie', 'result': False}
    ]

    expected_scores = ['green','yellow','red','red','critical','critical','red']

    result_stream = with_risk_scores(logs, employees_index, hosts_index, employees, hosts)
    actual_scores = [r['risk_score'] for r in result_stream]

    assert actual_scores == expected_scores

def test_with_risk_scores_fallback():
    # Ingen employees/hosts info -> fallback på result
    logs = [
        {'hostname': 'pc-001', 'timestamp': '2024-01-01', 'username': 'Alice', 'result': True},
        {'hostname': 'pc-001', 'timestamp': '2024-01-01', 'username': 'Bob', 'result': False},
    ]
    expected_scores = ['green','red']  # fallback
    result_stream = with_risk_scores(logs)
    actual_scores = [r['risk_score'] for r in result_stream]
    assert actual_scores == expected_scores


## OPGAVE 3 her

sample_log = [
    ('pc-001', '2025-11-01T08:00:00', 'root', 'success'),
    ('pc-002', '2025-11-01T09:00:00', 'alice', 'failure'),
    ('pc-003', '2025-11-01T10:00:00', 'bob', 'success'),
    ('pc-001', '2025-11-01T11:00:00', 'root', 'failure'),
    ('pc-002', '2025-11-01T12:00:00', 'alice', 'success'),
    ('pc-003', '2025-11-01T13:00:00', 'bob', 'failure'),
]

# --- Tests for count_root_login_attempts ---
def test_count_root_login_attempts_empty():
    assert count_root_login_attempts([]) == 0

def test_count_root_login_attempts_sample():
    assert count_root_login_attempts(sample_log) == 2

# --- Tests for count_login_attempts ---
def test_count_login_attempts_alice():
    assert count_login_attempts(sample_log, 'alice') == 2

def test_count_login_attempts_unknown_user():
    assert count_login_attempts(sample_log, 'eve') == 0

# --- Tests for count_login_attempts_by_user ---
def test_count_login_attempts_by_user():
    counts = count_login_attempts_by_user(sample_log)
    expected = {'root': 2, 'alice': 2, 'bob': 2}
    assert counts == expected

# --- Tests for login_stats_by_user ---
def test_login_stats_by_user_single_entry():
    single = [('pc-001', '2025-11-01T08:00:00', 'root', 'success')]
    stats = login_stats_by_user(single)
    expected = {
        'root': {'first': '2025-11-01T08:00:00', 'last': '2025-11-01T08:00:00',
                 'successes': 1, 'failures': 0}
    }
    assert stats == expected

def test_login_stats_by_user_multiple_entries():
    stats = login_stats_by_user(sample_log)
    expected = {
        'root': {'first': '2025-11-01T08:00:00', 'last': '2025-11-01T11:00:00', 'successes': 1, 'failures': 1},
        'alice': {'first': '2025-11-01T09:00:00', 'last': '2025-11-01T12:00:00', 'successes': 1, 'failures': 1},
        'bob': {'first': '2025-11-01T10:00:00', 'last': '2025-11-01T13:00:00', 'successes': 1, 'failures': 1}
    }
    assert stats == expected