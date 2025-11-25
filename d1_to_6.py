# Alle opgaver i d-serien

#Opgave d1_1 -- in_december -- login forsøg i december måned
def in_december(logs):
    for log in logs:
        timestamp = log[1]
        month = timestamp[5:7]
        if month == '12':
            yield log


#Opgave d1_2 -- in_date_range -- generalisering af tidligere opgave
def in_date_range(logs, start, end):
    for log in logs:
        timestamp = log[1]
        date = timestamp[:10]
        if start <= date <= end:
            yield log

#Opgave d1_3 -- on_host -- login på en given host
# Opgaven antager at input er på følgende form:
# (host, timestamp, username, success)
def on_host(stream, hostname):
    for record in stream:
        if record[0] == hostname:
            yield record
            
#Opgave d1_4 -- by_user -- login fra given bruger
def by_user(stream, username):
    for record in stream:
        if record[2] == username:
            yield record
          
# OPGAVE 2 HER FRA  

#Opgave d2_1 -- as_dicts -- afbild til datastrøm af ordbøger
def as_dicts(stream):
    for record in stream:
        yield{
            'hostname'  : record[0],
            'timestamp' : record[1],
            'username'  : record[2],
            'result'    : record[3]
        }

#Opgave d2_2 -- with_boolean_result -- lav succes og failure til bool
def with_boolean_results(stream):
    for record in stream:
        new_record = record.copy()
        if record['result'] == 'success':
            new_record['result'] = True
        else:
            new_record['result'] = False
        yield new_record

#Opgave d2_3 -- with_dates -- 
def with_dates(stream):
    for record in stream:
        new_record = record.copy()
        new_record['timestamp'] = record['timestamp'][:10]
        yield new_record

#Opgave d2_4 -- with_risk_scores -- ligesom opgave o2_5
def with_risk_scores(stream, employees_index=None, hosts_index=None, employees=None, hosts=None):

    for record in stream:
        hostname = record['hostname']
        username = record['username']
        # konverter result til 'success'/'failure' string hvis Boolean
        result_type = 'success' if record['result'] in [True, 'success'] else 'failure'

        score = None

        if employees_index and hosts_index and employees and hosts:
            if username in employees_index:
                emp = employees[employees_index[username]]
                emp_dept = emp[3]  # medarbejders afdeling

                if hostname in hosts_index:
                    host = hosts[hosts_index[hostname]]
                    host_dept = host[2]  # host-afdeling

                    if emp_dept == host_dept:
                        score = 'green'
                    else:
                        score = 'yellow' if result_type == 'failure' else 'red'
                else:
                    # host ukendt
                    score = 'red' if result_type == 'failure' else 'critical'
            else:
                # bruger ukendt
                score = 'red' if result_type == 'failure' else 'critical'
        else:
            # ingen info om employees/hosts, fallback baseret på success/failure
            score = 'green' if result_type == 'success' else 'red'

        new_record = record.copy()
        new_record['risk_score'] = score
        yield new_record


# Opgave 3 her fra

# Opgave d3_1 -- 
def count_root_login_attempts(stream):
    count = 0
    for record in stream:
        if record[2] == 'root':
            count += 1
    return count

# Opgave d3_2
def count_login_attempts(stream, username):
    count = 0
    for record in stream:
        if  record[2] == username:
            count +=1
    return count

# Opgave d3_3
def count_login_attempts_by_user(stream):
    counts = {}
    for record in stream:
        user = record[2]
        # returnerer eksisterende værdi eller 0, hvis brugeren ikke er i ordbogen endnu
        counts[user] = counts.get(user, 0) + 1
    return counts

# Opgave d3_4
def login_stats_by_user (stream):
    stats = {}
    for record in stream:
        user = record[2]
        timestamp = record [1]
        success = record[3] == 'success'
        
        if user not in stats:
            stats[user] = {
                'first'     : timestamp,
                'last'      : timestamp,
                'successes' : 1 if success else 0,
                'failures'   : 0 if success else 1
            }
        else:
            stats[user]['first'] = min(stats[user]['first'], timestamp)
            stats[user]['last'] = max(stats[user]['last'], timestamp)
            if success:
                stats[user]['successes'] += 1
            else:
                stats[user]['failures'] += 1
    return stats
"""
For hver bruger gemmer vi først first og last login, samt successes og failures.
min() og max() på timestamp-string virker her, fordi ISO 8601-datoer (yyyy-mm-ddThh:mm:ss) 
kan sammenlignes direkte som strenge.
På den måde får vi fuld oversigt over alle loginforsøg pr. bruger."""

