# 3 filtreringer, 1 afbildning og 1 reduktion

# De 3 filtreringer her:
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
          

#Opgave d2_3 -- with_dates -- 
def with_dates(stream):
    for record in stream:
        new_record = record.copy()
        new_record[0] = record[0][:10]
        yield new_record


# Reduktion her
# Opgave d3_2
def count_login_attempts(stream, username):
    count = 0
    for record in stream:
        if  record[2] == username:
            count +=1
    return count

def to_values(stream):
    for row in stream:
        yield row  # allerede en liste

def write_csv(stream_of_vectors, filename):
    import csv
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for v in stream_of_vectors:
            writer.writerow(v)

if __name__ == '__main__':
    import csv
    username_filter = 'nima'
    hostname_filter = 'pc-017'

    with open('auth_log.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        # 3 filtre
        stream = in_date_range(reader, '2024-01-01', '2025-12-12')
        stream = on_host(stream, hostname_filter)
        stream = by_user(stream, username_filter)

        # afbildning
        stream = with_dates(stream)

        # Gem resultatet til genbrug
        data = list(stream)

        # reduktion (printbart)
        login_count = count_login_attempts(data, username_filter)
        print(f'Login-forsoeg for {username_filter}: {login_count}')

        # skriv CSV
        stream = to_values(data)
        write_csv(stream, 'd4_2_filtered_auth_log.csv')

    # Grunden til "data = list(stream)" er fordi hvis vi først tømmer stream
    # så kan den ikke genbruges. 
    # Her bliver login forsøg printet i terminalen og resten står i 
    # CSV filen som er blevet lavet ved at køre koden. 
