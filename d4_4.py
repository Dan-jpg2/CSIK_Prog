# Da denne opgave beder om datstrøm kun med tekststrenge, har jeg lavet min 
# egen data og laver også nye funktioner her til i stedet for 
# at bruge de gamle.

# Filter funktion så vi kun beholder linjer med "password"
def contains_password(stream):
    for line in stream:
        if 'password' in line:
            yield line

# Afbildnings funktion til udtræk af I.P 
def get_ip(stream):
    for line in stream:
        parts = line.split(" from ")
        if len(parts) == 2:
            ip = parts[1]
        else:
            ip = "NO IP"
        yield ip

# Afbildning af handlingen 
def get_action(stream):
    for line in stream:
        if 'Accepted' in line:
            yield 'Accepted'
        elif 'Failed' in line:
            yield 'Failed'
        else:
            yield 'Other'

# Kombinere nu de to afbildninger data strømme til rækker
# Det en midlertidig liste til at holde de filtrerede linjer
def combine_to_rows(filtered_lines):
    lines = list(filtered_lines)
    
    actions = list(get_action(lines))
    ips = list(get_ip(lines))
    
    rows = []
    for i in range(len(lines)):
        rows.append([actions[i], ips[i]])
    return rows

# Den givede funktion fra opgaven
def write_csv(stream_of_vectors, filename):
    import csv
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for v in stream_of_vectors:
            writer.writerow(v)

if __name__ == '__main__':
    fake_logs = [
    "Accepted password for user1 from 192.168.1.10",
    "Failed password for root from 10.0.0.1",
    "User login attempt from 172.16.0.5",
    "Accepted password for user2 from 192.168.1.11",
    "Connection closed by 127.0.0.1",
    "Failed password for guest from 10.0.0.2"
    ]
    
    filtered = contains_password(fake_logs)
    rows = combine_to_rows(filtered)
    write_csv(rows, 'd4_4_filtered_auth_log.csv')
    
    