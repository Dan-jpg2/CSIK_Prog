from d1_to_3 import *

if __name__ == '__main__':
    import csv
    with open('auth_log.csv', 'r', newline='', encoding='utf-8') as in_file:
        with open('filtered_auth_log.csv', 'w', newline='', encoding='utf-8') as out_file:
            reader = csv.reader(in_file)
            writer = csv.writer(out_file)
            for log in in_date_range(reader, '2025-11-01', '2025-11-30'):   # Ændre funktions navn her samt diverse input som den tager og køre,
                                                                            # Du vil se funktions funktionalitet i den nye fil "filtered_auth_log"
                writer.writerow(log)