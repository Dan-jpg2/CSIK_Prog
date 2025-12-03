# Vælger at ændre pipelines fra opgave d4_1
# Bruger in_december og on_host
# Dertil with_dates
    
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
        stream = (x for x in reader if x[1][5:7] == '12') # Filtrerer kun til december måned (in_december)
        stream = (x for x in stream if x[0] == hostname_filter) # Kun richard som host (on_host)
        stream = (x for x in stream if x[1][:10])
        write_csv(stream, 'd5_1_filtered_auth_log.csv')