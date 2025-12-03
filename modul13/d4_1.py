def in_december(logs):
    for log in logs:
        timestamp = log[1]
        month = timestamp[5:7]
        if month == '12':
            yield log

def on_host(stream, hostname):
    for record in stream:
        if record[0] == hostname:
            yield record

def with_dates(stream):
    for record in stream:
        new_record = record[:]  # lav en kopi af listen
        new_record[1] = record[1][:10]  # ændr timestamp
        yield new_record

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
    hostname_filter = 'richard' # <- juster til din given host
    import csv
    with open('auth_log.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        stream = in_december(reader) # Filtrerer kun til december måned
        stream = on_host(stream, hostname_filter) # Kun til en given host
        stream = with_dates(stream) # Vil kune have dato og ikke tidspunkt
        stream = to_values(stream)
        write_csv(stream, 'd4_1_filtered_auth_log.csv')
