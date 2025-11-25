from v4_2 import root_login_attempts_of, month_of, summary_of

def test_root_login_attempts_of():
    logs = [
        ('2025-01-12T12:00:00', 'root', 'failure'),
        ('2025-01-12T12:10:00', 'root', 'success'),
        ('2025-01-12T12:20:00', 'admin', 'failure'),
        ('2025-01-12T12:30:00', 'root', 'failure'),
    ]
    expected = [
        ('2025-01-12T12:00:00', 'root', 'failure'),
        ('2025-01-12T12:30:00', 'root', 'failure')
    ]
    assert root_login_attempts_of(logs) == expected

    # tom liste giver tomt resultat
    assert root_login_attempts_of([]) == []


def test_month_of():
    logs = [
        ('2025-01-12T12:00:00', 'root', 'failure'),
        ('2025-02-15T10:30:00', 'root', 'failure'),
        ('2025-12-25T23:59:59', 'root', 'failure')
    ]
    expected = [1, 2, 12]
    assert month_of(logs) == expected

    # tom inputliste
    assert month_of([]) == []


def test_summary_of():
    months = [1, 1, 2, 12, 12, 12]
    # Januar (1) = 2, Februar (2) = 1, December (12) = 3
    expected = [2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3]
    assert summary_of(months) == expected

    # tom liste giver nul for alle måneder
    assert summary_of([]) == [0] * 12


def test_integration():
    logs = [
        ('2025-01-05T09:10:00', 'root', 'failure'),
        ('2025-02-10T11:20:00', 'admin', 'failure'),
        ('2025-02-15T12:30:00', 'root', 'failure'),
        ('2025-02-17T13:40:00', 'root', 'success'),
        ('2025-03-01T08:00:00', 'root', 'failure')
    ]

    filtered = root_login_attempts_of(logs)
    months = month_of(filtered)
    summary = summary_of(months)

    # root + failure kun i jan, feb og mar
    expected_summary = [1, 1, 1] + [0] * 9
    assert summary == expected_summary
