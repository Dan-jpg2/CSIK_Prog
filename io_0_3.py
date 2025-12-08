import sqlite3

with sqlite3.connect("hvedebro.sqlite") as connection:
    
    while True:
        username = input("Hvilket brugernavn vil du se logins for? (q for quit) ")
        
        if username == "q":
            print("Ses på grillen")
            break
        
        count_str = input("Hor mange login forsøg skal der hentes? ")
        count = int(count_str)
        
        stream = connection.execute(
            """
            select 
                h.name as hostname,
                a.timestamp,
                a.result
            from auth_logs a
            join hosts h using (host_id)
            where a.username = ?
            order by a.timestamp
            limit ?

            
            
            """,
            (username, count) # ? bruges så vi sikre os mod sql injektion
        )
    
        print("\nLoginforsøg: ")
        for hostname, ts, result in stream:
            print(f"{ts} - {hostname} - {result}")
        print()