from d1_to_3 import *

if __name__ == '__main__':
    import csv
    with open('auth_log.csv', 'r', newline='', encoding='utf-8') as in_file, \
         open('processed_auth_log.csv', 'w', newline='', encoding='utf-8') as out_file:

        reader = csv.reader(in_file)
        writer = csv.DictWriter(out_file, fieldnames=['hostname','timestamp','username','result','risk_score'])
        writer.writeheader()

        stream = as_dicts(reader)
        stream = with_boolean_results(stream)
        stream = with_dates(stream)
        stream = with_risk_scores(stream)

        for record in stream:
            writer.writerow(record)
            