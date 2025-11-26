## 2 filtreringer og 2 afbildninger

#Opgave d1_3 -- on_host -- login på en given host
# Opgaven antager at input er på følgende form:
# (host, timestamp, username, success)
#Filter
def on_host(stream, hostname):
    for record in stream:
        if record[0] == hostname:
            yield record
            
#Opgave d1_4 -- by_user -- login fra given bruger
# Filter
def by_user(stream, username):
    for record in stream:
        if record[2] == username:
            yield record
            
#Opgave d2_1 -- as_dicts -- afbild til datastrøm af ordbøger
#Afbildning
def as_dicts(stream):
    for record in stream:
        yield{
            'hostname'  : record[0],
            'timestamp' : record[1],
            'username'  : record[2],
            'result'    : record[3]
        }

# Afbildning
#Opgave d2_3 -- with_dates -- 
def with_dates(stream):
    for record in stream:
        new_record = record.copy()
        new_record['timestamp'] = record['timestamp'][:10]
        yield new_record
        

# Da jeg vælger at bruge min "as_dict" som laver det om til en dictionary
# bliver jeg nød til at ændre i denne kode da jeg kun får keys som en 
# tekst streng 
def to_values(stream):
    for row in stream:
        yield row.values()  # Ændre her fra row -> row.values()

def write_csv(stream_of_vectors, filename):
    import csv
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for v in stream_of_vectors:
            writer.writerow(v)

if __name__ == '__main__':
    import csv
    username_filter = 'ereg'
    hostname_filter = 'pc-022'
    
    with open('auth_log.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
    
        # 2 filtre
        stream = on_host(reader, hostname_filter)
        stream = by_user(stream, username_filter)
        
        #2 afbildninger
        stream = as_dicts(stream)
        stream = with_dates(stream)
        data = list(stream)
        
        stream = to_values(data)        
        write_csv(stream, 'd4_3_filtered_auth_log.csv')
    