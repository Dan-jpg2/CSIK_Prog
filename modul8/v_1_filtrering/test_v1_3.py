from v1_3 import suspicious_login_attempts_of

def test_suspicious_login_attempts_of():
    data = [        
        ('2025-10-30T07:25:14', 'root', False),
        ('2025-10-30T07:26:04', 'admin', False),
        ('2025-10-30T07:28:14', 'root', True),
        ('2025-10-30T07:32:16', 'root', False)    
        ]
    assert suspicious_login_attempts_of(data) == [
        ('2025-10-30T07:25:14', 'root', False),
        ('2025-10-30T07:32:16', 'root', False)
    ]
    assert suspicious_login_attempts_of([]) == []
    assert suspicious_login_attempts_of([
        ('2025-10-30T07:30:00', 'user', True)
    ]) == []