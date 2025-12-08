import sqlite3

with sqlite3.connect('hvedebro.sqlite') as connection:
    connection = connection.cursor()
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
    
    col_name = tuple(d[0] for d in stream.description)
    print(col_name)
    for row in stream:
        print({col_name[i]: row[i] for i in range(len(col_name))})
   