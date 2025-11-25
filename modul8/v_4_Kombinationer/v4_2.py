import csv

# Vores filter med kun 'root' brugernavn

def is_failing_root_login(log):
    return log[1] == 'root' and log[2] == 'failure'

def root_login_attempts_of(logs):
        return filtered(is_failing_root_login, logs)

def filtered(f, v):
    result = []
    n = len(v)
    i = 0
    while i < n:
        if f(v[i]):
            result.append(v[i])
        i = i + 1
    return result



# Vores afbildning login forsøg
def month_of(logs):
    n = len(logs)
    result = [None] * n
    i = 0
    while i < n:
        timestamp, _, _ = logs[i]
        result[i] = int(timestamp[5:7])
        i = i +1
    return result

# Reducering af logs
def summary_of(months):
    n = len(months)
    counts = [0] * 12
    i = 0
    while i < n:
        counts[months [i] - 1] = counts[months[i] - 1] + 1
        i = i + 1
    return counts

if __name__ == '__main__':
    with open('auth_log_2024.csv', 'r') as file:
        logs = list(csv.reader(file))
        print(summary_of(month_of(root_login_attempts_of(logs))))
