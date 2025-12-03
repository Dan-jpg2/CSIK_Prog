import sqlite3

with sqlite3.connect('hvedebro.sqlite') as connection: # Ændre lidt i hvilke data der udtrækkes og se på Canvas for oversigten.
    stream = connection.execute(
        """
        select 
            department_id, last_day
        from employees    
        
        
        """)
    print(next(stream)) 
    print(next(stream)) 
    print(next(stream)) 
    
    # svar på spørgsmål:
"""     Kolonne                   Forklaring                                                               
| -------------------- | --------------------------------------------------------------------------- |
| department_id        | NULL fordi personen ikke længere hører til en afdeling                      |
| last_day             | Dato for hvornår personen stoppede                                          |
| former_employees.csv | Indeholder den samme type data → bekræfter at employees = tidligere ansatte |

"""