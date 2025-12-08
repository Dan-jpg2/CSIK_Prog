import sqlite3


# Opgave 1
with sqlite3.connect('hvedebro.sqlite') as connection:
    stream = connection.execute(
    """
    select * 
    from employees
    where username in ('poul', 'fatter')
    
    """
    )   
for row in stream:
    print(row)
    
# Data formen er:
# employees   employee_id   integer
#             name           text
#             cpr            text
#             username       text
#             department_id  integer
#             last_day       date

# (7049, 'Hans F�tter', '110568-0589', 'fatter', 80, None)
# (7046, 'Poul Nielsen', '141187-0417', 'poul', 81, None)


"""Opgave 2:
I hosts-tabellen er både host_id (surrogatnøgle) og mac (naturlig nøgle) rimelige nøgler.
I auth_logs findes ingen entydig nøgle — tabellen er en log, 
og ingen kolonner eller kombinationer garanterer unikhed.

Opgave 3:
Tre tabeller har primærnøgler, alle surrogatnøgler af typen integer:

departments -> department_id

hosts -> host_id

employees -> employee_id

auth_logs har ingen primærnøgle."""