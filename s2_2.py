import sqlite3

with sqlite3.connect('hvedebro.sqlite') as connection: 
    stream = connection.execute(
        """
          select 
                    d.name as department_name, h.name as hostname, h.mac
          from departments d
          join hosts h using (department_id)
        
        
        """)
    for row in stream:
        print(row)

"""
d og h er aliases for tabellerne departments og hosts
Det gør det bare nemmere at refferere til kolonnerne, specielt når tabellerne har lange navne
"""