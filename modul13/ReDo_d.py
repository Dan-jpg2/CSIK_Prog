#d1_1
def in_december(logs):
    for log in logs:
        timestamp = log[1]
        month = timestamp[5:7]
        if month == '12':
            yield log

# d1_2
def in_date_range(logs, start, end):
    for log in logs:
        timestamp = log[1]
        date = timestamp[:10]
        if start <= date <= end:
            yield log

# d1_3
def on_host(stream, hostname):
    for log in stream:
        host = log[0]
        if hostname == host:
            yield log

# d1_4
def by_user(stream, username):
    for record in stream:
        if record[2] == username:
            yield record

# d2_1 
def as_dicts(stream):
    for log in stream:
        yield {
                'hostname'  :log[0],
                'timestamp' :log[1],
                'username'  :log[2],
                'result'    :log[3]
        }

# d2_2
def with_boolean_results(stream):
    for log in stream:
        if log['result'] == 'success':
            yield True
        else:
            yield False

# d2_3
def with_dates(stream):
    pass
# kommentar