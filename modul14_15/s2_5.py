import sqlite3

with sqlite3.connect('hvedebro.sqlite') as connection:
    stream = connection.execute(
    """
        select 
            e.name,
            e.cpr,
            e.username,
            d.name as department_name
        from employees e
        join departments d using (department_id)
        where e.last_day is null
        order by e.employee_id
            
    """
    )
    for row in stream:
        print(row)