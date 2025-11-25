from itertools import groupby
from operator import itemgetter



def daily_ohlc(data):
    if not data:
        return []

    result = []
    current_date = data[0][0]
    prices = []

    for date, time, price in data:
        if date != current_date:
            # Når datoen skifter, gem resultatet for den forrige dag
            result.append((
                current_date,
                prices[0],          # Open
                max(prices),        # High
                min(prices),        # Low
                prices[-1]          # Close
            ))
            # Start på ny dag
            current_date = date
            prices = []
        prices.append(price)

    # Tilføj sidste dags data
    result.append((
        current_date,
        prices[0],
        max(prices),
        min(prices),
        prices[-1]
    ))

    return result



#Optimeret version ved brug af groupby da vi ved at vi får en sorteret liste.
def daily_ohlc_optimized(records):
    result = []
    for date, group in groupby(records, key=itemgetter(0)):
        prices = [price for _, _, price in group]
        open_ = prices[0]
        high = max(prices)
        low = min(prices)
        close = prices[-1]
        result.append((date, open_, high, low, close))
    return result