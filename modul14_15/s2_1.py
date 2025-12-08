import sqlite3

#Opgave 1
# Identificér to andre fremmednøgler i databasen. 
# Hvilke sammenhænge mellem tabeller beskriver de?

"""
Fremmednøgle 1

employees.department_id → departments.department_id

Sammenhæng:

Én afdeling har nul eller flere ansatte

Hver ansat tilhører nøjagtig én afdeling
→ Én-til-mange relation: “afdelingen har ansatte” / “ansat tilhører afdeling”

Fremmednøgle 2

auth_logs.host_id → hosts.host_id

Sammenhæng:

Hver log-linje er et login-forsøg på en bestemt host

En host kan have mange auth log entries
→ Én-til-mange relation: “maskine har log-entries” / “log bekymrer en bestemt maskine”




"""