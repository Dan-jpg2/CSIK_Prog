

##### opgave o0 #####

## o0_1     leg med ordbøgerne

## o0_2     
#Hvordan danner du en tom ordbog og 
# tilordner en reference til den til en variabel

# // d = {}
# eller
# // d = dict()
# Begge peger på en tom ordbog 

#####   ----- Opgaver o1 ----- #####

##### o1_1 ----- index_of #####
def index_of(v):
    d = {}
    n = len(v)
    i = 0
    while i < n:
        d[v[i]] = i
        i = i + 1
    return d

#Obligatorisk 1-liner
def one_liner_index_of(v):
    return {x: i for i, x in enumerate(v)}

##### o1_2 ----- mac_index_of #####
def mac_index_of(v):
    d = {}
    n = len(v)
    i = 0
    while i < n:
        mac_address = v[i][3]
        d[mac_address] = i
        i = i + 1
    return d 

##### o1_3 ----- mac_index_of_expanded ##### Udividdet version 
def mac_index_of_expanded(v):
    d = {}
    n = len(v)
    i = 0
    while i < n:
        mac_address = v[i][3]
        if mac_address in d:
            raise ValueError(f'Duplicate MAC addess: {mac_address}')
        d[mac_address] = i
        i = i + 1
    return d 



##### o1_4 ----- omskrivning af o1_3 #####
def mac_index_of_expanded_further(v):
    d = {}
    n = len(v)
    i = 0
    while i < n:
        mac_address = v[i][3]
        value = v[i][0:3]
        if mac_address in d:
            raise ValueError(f'Duplicate MAC addess: {mac_address}')
        d[mac_address] = value
        i += 1
    return d

#####   -----   Opgave o2 og frem ----- #####

##### ----- o2_1 ----- username index #####
# Der skal her bruges former_employees.csv filen til test

def username_index_of(former_employees):
    d = {}
    n = len(former_employees)
    i = 0
    while i < n:
        username = former_employees[i][2]
        if username in d:
            raise ValueError(f"Dublicate username found: {username}")
        d[username] = i
        i += 1
    return d

##### ----- o2_2 ----- post termination logs #####
# Bruge username_index_of(former_employees) → giver en ordbog med username -> indeks.
#Gennemløbe auth_log.
#For hvert login:
#   Tjek om brugeren findes i former_employees.
#   Sammenlign tidspunktet (timestamp) med medarbejderens termination_date.
#   Hvis login er efter sidste arbejdsdag → gem det i resultatlisten.

def post_termination_logins_of(former_employees, auth_log):
    index = username_index_of(former_employees)

    result = []
    n = len(auth_log)
    i = 0
    
    while i < n:
        (hostname, timestamp, username, result_code) = auth_log[i]
        if username in index:
            
            (name, cpr, username, termination_date) = former_employees[index[username]]
            
            if timestamp > termination_date:
                result.append(auth_log[i])
        i += 1
    return result 

##### ----- o2_3 ----- employee index of #####
# Genbruger bare koden fra opbage 2 med en specialisering i input?
def employee_index_of(employees):
    return username_index_of(employees)

##### ----- o2_4 ---- hostname_index_of #####
def hostname_index_of(hosts):
    d = {}
    n = len(hosts)
    i = 0
    while i < n:
        hostname = hosts[i][0]
        d[hostname] = i
        i += 1
    return d

##### ----- o2_5 ---- risk_score_of #####
def risk_score_of(auth_log, employees_index, hosts_index, employees, hosts):
    n = len(auth_log)
    result = [None] * n
    i = 0

    while i < n:
        hostname, _, username, result_type = auth_log[i]

        # Default score — hvis intet passer
        score = None

        # Se om brugeren findes blandt ansatte
        if username in employees_index:
            emp = employees[employees_index[username]]
            emp_dept = emp[3]  # afdeling

            # Se om computeren findes i hosts-listen
            if hostname in hosts_index:
                host = hosts[hosts_index[hostname]]
                host_dept = host[2]  # afdeling

                if emp_dept == host_dept:
                    # Samme afdeling
                    score = 'green'
                else:
                    # Forskellige afdelinger
                    if result_type == 'failure':
                        score = 'yellow'
                    else:
                        score = 'red'
            else:
                # Host ikke kendt
                if result_type == 'failure':
                    score = 'red'
                else:
                    score = 'critical'
        else:
            # Ukendt bruger
            if result_type == 'failure':
                score = 'red'
            else:
                score = 'critical'

        result[i] = score
        i += 1

    return result

##### ----- o2_6 ---- risk_summary_of #####

def risk_summary_of(auth_log, risk_scores):
    red_count = 0
    critical_count = 0
    first_timestamp = None
    last_timestamp = None

    n = len(auth_log)
    i = 0
    while i < n:
        (_, timestamp, _, _) = auth_log[i]
        score = risk_scores[i]

        if score == 'red' or score == 'critical':
            # tæller bare op
            if score == 'red':
                red_count += 1
            else:
                critical_count += 1
            
            # Første forekomst (timestamp)
            if first_timestamp is None:
                first_timestamp = timestamp

            # Den sidste timestamp, som opdateres løbende
            last_timestamp = timestamp
        i += 1
    return (red_count, critical_count, first_timestamp, last_timestamp)

#####   -----   Opgave o3 og frem ----- #####

##### ----- o3_1 ----- failed_login_count_by_username #####

#Bruger kodeskabelon B da vi skal initialisere hver bruger,
# første gang vi støder på dem
def failed_login_count_by_username(auth_log):
    n = len(auth_log)
    d = {}
    i = 0
    while i < n:
        (_, _, username, result) = auth_log[i]

        if username not in d:
            #første gang vi ser brugeren, starter vi tælling
            d[username] = 1 if result == 'failure' else 0
        else:
            # senere, tæl kun hvis fejl
            if result == 'failure':
                d[username] = d[username] + 1
        i += 1
    return d

##### ----- o3_2 ----- login_dates_by_username #####
#kodeskabelon A da vi kan initialisere uden første element
def login_dates_by_username(auth_log):
    n = len(auth_log)
    d = {}
    i = 0
    while i < n:
        (_, timestamp, username, _) = auth_log[i]
        date = timestamp.split("T")[0]  # udtræk dato-delen
        
        if username not in d:
            d[username] = []  # initialiser tom liste
        # Tilføj datoen til brugerens liste
        d[username].append(date)
        i = i + 1
    return d

##### ----- o3_3 ----- failed_logins_by_user #####
#kodeskabelon A da vi kan initialisere uden første element
def failed_logins_by_username(auth_log):
    n = len(auth_log)
    d = {}
    i = 0
    while i < n:
        hostname, timestamp, username, result = auth_log[i]

        # kun filtrer de fejlende logins
        if result != 'success':
            if username not in d:
                d[username] = []
            d[username].append(auth_log[i]) #tilføjer de fejlende forsøg   
        i += 1
    return d

##### ----- o3_4 ----- active_period_by_username #####
# Bruger skabelon B da vi skal initialisere ud fra første element
def active_period_by_username(auth_log):
    n = len(auth_log)
    d = {}
    i = 0
    while i < n:
        hostname, timestamp, username, result = auth_log[i]

        if username not in d:
            #første login for brugeren
            d[username] = (timestamp, timestamp)
        else:
            #opdatere første og sidste login
            first, last = d[username]
            if timestamp < first:
                first = timestamp
            if timestamp > last:
                last = timestamp
            d[username] = (first, last)
        i += 1
    return d

##### ----- o3_5 ----- stats_by_hostname #####

def stats_by_hostname(auth_log):
    n = len(auth_log)
    d = {}
    i = 0 
    while i < n:
        hostname, timestamp, username, result = auth_log[i]

        if hostname not in d:
            #her er første gang vi ser dette hostname
            d[hostname] = (timestamp, timestamp, 1)
        else:
            first, last, count = d[hostname]
            if timestamp < first:
                first = timestamp
            if timestamp > last:
                last = timestamp
            count += 1
            d[hostname] = (first, last, count)
        i += 1
    #omdanner ordbogen til en liste (tuples)
    result = []
    for hostname in d:
        first, last, count = d[hostname]
        result.append((hostname, first, last, count))
    return result

##### ----- o3_6 ----- stats_by_hostname_and_username #####
# Bruger skabelon B da vi skal bruge første element
def stats_by_hostname_and_username(auth_log):
    n = len(auth_log)
    d = {}
    i = 0
    while i < n:
        hostname, timestamp, username, result = auth_log[i]
        key = (hostname, username)
        if key not in d:
            d[key] = (timestamp, timestamp, 1)
        else:
            first, last, count = d[key]
            if timestamp < first:
                first = timestamp
            if timestamp > last:
                last = timestamp
            count += 1
            d[key] = (first, last, count)
        i += 1

    #Omdanner ordbogen til liste
    result = []
    for (hostname, username), (first, last, count) in d.items():
        result.append((hostname, username, first, last, count))
    return result
        
##### ----- o4 opgaver her fra ----- #####
# For defineret funktion som skal danne test data.

import random
from datetime import datetime, timedelta

CURRENCIES = ['ETH', 'USDT', 'BNB', 'USDC', 'WBTC', 'LINK', 'BAT']
ADDRESSES = ['a03f', 'b077', 'c0da', 'd084', 'e0fe', 'f052']

def random_transfers(n, start='2015-07-01', end=None):
    start_time = datetime.fromisoformat(start)
    end_time = datetime.fromisoformat(end) if end else datetime.today()
    if end_time <= start_time:
        raise ValueError('start must be before end')
    seconds = int((end_time - start_time).total_seconds())
    result = []
    i = 0
    while i < n:
        time = start_time + timedelta(seconds=random.randint(0, seconds))
        currency = random.choice(CURRENCIES)
        amount = random.randint(1, 10)
        sender = random.choice(ADDRESSES)
        receiver = random.choice(ADDRESSES)
        result.append((
            time.isoformat(),
            currency,
            amount,
            sender,
            receiver,
        ))
        i += 1
    return result

##### ----- o4_1 ----- count_by_currencies #####
def count_by_currency(transfers):
    n = len(transfers)
    d = {}
    i = 0
    while i < n:
        _, currency, _, _, _ = transfers[i]
        if currency not in d:
            d[currency] = 0
        d[currency] += 1
        i += 1
    return d

##### ----- o4_2 ----- count_by_date #####
def count_by_date(transfers):
    n = len(transfers)
    d = {}
    i = 0
    while i < n:
        timestamp = transfers[i][0]
        date = timestamp[:10] # eller timestamp.split("T")[0]
        if date not in d: 
            d[date] = 1
        else:
            d[date] += 1
        i += 1
    return d

##### ----- o4_3 ----- sum_by_date_and_currency #####
def sum_by_date_and_currency(transfers):
    n = len(transfers)
    d = {}
    i = 0
    while i < n:
        timestamp, currency, amount, sender, receiver = transfers[i]
        date = timestamp[:10]
        key = (date, currency)
        if key not in d:
            d[key] = amount
        else:
            d[key] += amount
        i += 1
    return d

##### ----- o4_4 ----- active_timespan_by_address #####
def active_timespan_by_address(transfers):
    n = len(transfers)
    d = {}
    i = 0
    while i < n:
        timestamp, currency, amount, sender, receiver = transfers[i]

        for addr in (sender, receiver):
            if addr not in d:
                d[addr] = (timestamp, timestamp)
            else:
                first, last = d[addr]
                if timestamp < first:
                    first = timestamp
                if timestamp > last:
                    last = timestamp
                d[addr] = (first, last)
        i += 1
    return d

##### ----- o4_5 ----- net_inflow_by_address_and_currency #####
def net_inflow_by_address_and_currency(transfers):
    d = {}
    for timestamp, currency, amount, sender, receiver in transfers:
        # Spring helt over hvis sender og receiver er den samme adresse
        if sender == receiver:
            continue
        # Afsender mister beløb
        sender_key = (sender, currency)
        d[sender_key] = d.get(sender_key, 0) - amount

        #Modtager får beløbet
        if receiver != sender:
            receiver_key = (receiver, currency)
            d[receiver_key] = d.get(receiver_key, 0) + amount
        
    
    return d

##### ----- o5 har fået sin egen fil ----- #####