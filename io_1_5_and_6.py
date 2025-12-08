import sqlite3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("db_path", help="Sti til din SQL database")
parser.add_argument("--limit", "-l", type=int, default=20, help="antal loginforsøg der skal hentes (default: 20)") 
# Laver et optionelt limit med --limit (opgave 5) og laver en forkortelse "-l" (opgave 6)
args = parser.parse_args()

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
        (args.limit,)
    )
    for row in stream:
        print(row)