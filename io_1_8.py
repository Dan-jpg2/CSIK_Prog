import sqlite3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("db_path", help="Sti til din SQL database")
parser.add_argument("--limit", "-l", type=int, default=20, help="Antal loginforsøg der skal vises (default: 20)")
parser.add_argument("--host", default="all", help="filter på værtsnavn (hostname)")
parser.add_argument("--user_department", default="all", help="filter på medarbejderens afdeling (department)")
args = parser.parse_args()

with sqlite3.connect(args.db_path) as connection:
    stream = connection.execute(
        """
        select 
            h.name as hostname,
            a.username,
            a.timestamp,
            a.result,
            d.name as department_name
        from auth_logs a
        join hosts h using (host_id)
        join employees e using (username)
        join departments d using (department_id)
        where   (? = 'all' or h.name = ?)
        and     (? = 'all' or d.name = ?)
        limit ?
        
        """,
        (args.host, args.host,
         args.user_department, args.user_department,
         args.limit)
    ) 
    # Joiner nu employees og departments ved auth_logs -> employees via username 
                                                        #   employees -> departments via department_id
    # Bruger samme where logik fra sidste opgave men nu på department name
    for row in stream:
        print(row)