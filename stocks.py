def calculateprofit(price_array):
    profit = 0
    length = len(price_array)
    i = 0

    while i < length:
        maximum = max(price_array[i:])
        if maximum - price_array[i] > profit:
            profit = maximum - price_array[i]
        i += 1

    return profit
