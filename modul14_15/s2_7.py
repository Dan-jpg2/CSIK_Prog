import sqlite3

with sqlite3.connect("hvedebro.sqlite") as connection:
    stream = connection.execute(
        """
        select d.name as department_name, h.name as hostname, a.timestamp, a.result
        from departments d
        join hosts h using (department_id)
        join auth_logs a using (host_id)
        """
    )
    print(next(stream))
    print(next(stream))
    

# Svar på spørgsmålene her:

"""
Hvad gør forespørgslen?

departments -> hosts
Giver én række for hver host i en afdeling.

hosts -> auth_logs
Giver én række for hver auth-log, der hører til en host.

Resultatet er derfor alle auth-login events, udvidet med hostens afdeling.

Hvor mange rækker får man? 
n_d = antal rækker i departments

n_h = antal rækker i hosts, hvor hver host tilhører præcis én department

n_a = antal rækker i auth_logs, hvor hver log-linje refererer til præcis én host

Derfor får man antal rækker som der er i auth_logs,
fordi hver auth_log event matcher nøjagtigt en host.
og hver host matcher nøjagtigt én department,
derfor bliver hver auth_log række til en udviddet række bestående af:
auth_log 1 ..... 1 hosts 1 ..... 1 departments
"""
