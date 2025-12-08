import sqlite3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("db_path", help="Sti til din SQL database")
parser.add_argument("--limit", "-l", type=int, default=20, help="antal loginforsøg der skal vises (default: 20)")
parser.add_argument("--host", default="all", help="filter på værtsnavn (hostname)")
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
        where (? = 'all' or h.name = ?)
        limit ?
        
        """,
        (args.host, args.host, args.limit)
    ) # Er lidt usikker på om syntaksen for where kan gøres bedre / mere sikker??
    for row in stream:
        print(row)