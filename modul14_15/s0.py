# Opgave 1 får nedenstående til at køre

# Filen 'hvedebro.sqlite' indeholder samme data som følgende:
# hosts.csv , employees.csv , former_employees.csv , auth_log.csv
# Filen er binær DONT OPEN IT
# 

import sqlite3

with sqlite3.connect('hvedebro.sqlite') as connection:
    stream = connection.execute('select name, mac from hosts')
    print(next(stream)) # ('mercury', 'd0:ad:08:e8:60:b1')
    print(next(stream)) # ('venus', 'd0:ad:08:e8:60:b2')
    print(next(stream)) # ('earth', 'd0:ad:08:e8:60:b3')
    
##### Opgave 1 - tjek #####

