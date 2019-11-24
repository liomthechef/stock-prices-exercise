def calculateprofit(price_array):
    length = len(price_array)
    i = 0
    # impracticably low integer to handle lossmaking.
    profit = -999999999

    if length < 2:
        raise Exception('length of input stock must be greater than 1')

    # max the stock price from next indice onwards
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
    if results[0] <= 0:
        print("trade is not profitable")
    else:
        print("trade is profitable")
