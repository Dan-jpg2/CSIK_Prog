import sqlite3

with sqlite3.connect('hvedebro.sqlite') as connection:
    stream = connection.execute(
        """
        with risk_scores as (
                    select
            a.host_id,
            h.name as hostname,
            a.timestamp,
            a.username,
            a.result,
            e.department_id as employee_department,
            h.department_id as host_department,
            case
                when e.last_day is null
                    and h.department_id = e.department_id
                then 'green'
                
                when e.last_day is null
                    and h.department_id <> e.department_id
                    and a.result = 0
                then 'yellow'
                
                when e.last_day is null
                    and h.department_id <> e.department_id
                    and a.result = 1
                then 'red'
                
                when a.result = 0
                then 'red'
                
                else 'critical'
            end as risk_color
        from auth_logs a
        left join employees e using (username)
        left join hosts h using (host_id)
        )
        select 
            sum(risk_color = 'red')          as red_count,
            sum(risk_color = 'critical')    as critical_count,
            min(case when risk_color = 'critical' then timestamp end) as first_critical,
            max(case when risk_color = 'critical' then timestamp end) as last_critical
        from risk_scores;
        
        
        """
    )
    for row in stream:
        print(row)