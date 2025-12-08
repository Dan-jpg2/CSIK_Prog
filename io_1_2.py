import sqlite3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("db_path")
parser.add_argument("limit")
args = parser.parse_args()

limit = int(args.limit) #Manuelt cast?

with sqlite3.connect(args.db_path) as connection:
    stream = connection.execute(
        """
        select 
            h.name as hostname,
            a.username,
            a.timestamp,
            a.result
        from auth_logs a
        join hosts h using (host_id)
        limit ?
        """,
        (limit,) # undgår sql injection
    )
    for row in stream:
        print(row)
        
    # Køres ved at kalde vores tidligere opgave "py io_1_1.py hvedebro.sqlite 20"
    # Her er hvedebro.sqlite vores db argument og 20 er vores limit argument