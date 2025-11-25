def suspicious_login_attempts_of(v):
    result = []
    n = len(v)
    i = 0
    while i < n:
        timestamp, username, success = v[i]
        if username == 'root' and success == False:
            result.append(v[i])
        i = i + 1
    return result