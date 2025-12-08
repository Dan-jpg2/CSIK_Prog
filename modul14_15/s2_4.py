import sqlite3

with sqlite3.connect('hvedebro.sqlite') as connection:
    stream = connection.execute(
        """
        select 
            h.name as hostname,
            h.mac, 
            d.name as department_name
        from hosts h
        join departments d using (department_id)
        order by h.name
        """
    )
    for row in stream:
        print(row)
        
