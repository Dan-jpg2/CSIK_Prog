import sqlite3

with sqlite3.connect('hvedebro.sqlite') as connection:
    stream = connection.execute(
    """
        select 
            a.host_id,
            a.timestamp,
            a.username,
            a.result,
            e.name as employee_name,
            e.last_day
        from auth_logs a
        join employees e using(username)
        where e.last_day is not null
            and a.timestamp > e.last_day
        order by a.timestamp
    """
    )
    for row in stream:
        print(row)