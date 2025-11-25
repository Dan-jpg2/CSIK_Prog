from itertools import accumulate

def moving_avg_of(v, window=3):
    if not v:
        return []
    result = []
    for i in range(len(v)):
        # det vindue vi arbejder i - altså de seneste 3 elementer
        window_vals = v[max(0, i - window + 1) : i + 1]
        # gennemsnittet beregnes af de værdier
        result.append(sum(window_vals) / len(window_vals))
    return result

