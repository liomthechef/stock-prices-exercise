def calculateprofit(price_array):
    length = len(price_array)
    i = 0
    profit = -999999

    while i + 1 < length:
        maximum = max(price_array[1+i:])
        if maximum - price_array[i] > profit:
            profit = maximum - price_array[i]
            buyprice = price_array[i]
            sellprice = maximum
        i += 1

    return profit, buyprice, sellprice


if __name__ == "__main__":
    results = calculateprofit([3, 4, 7, 12, 2, 5, 14, 27, 3, 1])
    print("profit is " + str(results[0]) + " buy price is " + str(results[1])
          + " sell price is " + str(results[2]))
