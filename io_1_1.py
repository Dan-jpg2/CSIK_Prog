import sqlite3

# Skal grænsen på limit 20 være justerbar eller?

with sqlite3.connect('hvedebro.sqlite') as connection:
    stream = connection.execute(
        """
        select 
            h.name as hostname,
            a.username,
            a.timestamp,
            a.result
        from auth_logs a
        join hosts h using (host_id)
        limit 20
        
        """
    )
    print('Hostname - username - timestamp - result')
    for row in stream:
        print(row)