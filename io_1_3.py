import sqlite3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("db_path")
parser.add_argument("limit", type=int)
args = parser.parse_args()

# limit = int(args.limit) Denne manuelle cast er fjernet og nubruger vi det blot i parseren linje 6 "type = int"

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
        (args.limit,) # undgår sql injection
    )
    for row in stream:
        print(row)
        