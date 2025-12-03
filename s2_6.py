import sqlite3

with sqlite3.connect('hvedebro.sqlite') as connection:
    stream = connection.execute(
    """
        select 
            h.name as hostname,
            a.timestamp,
            a.username,
            a.result
        from auth_logs a
        join hosts h using (host_id)
        order by a.timestamp
    """
    )
    
    print(next(stream))
    print(next(stream))