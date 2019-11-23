price_array = [2,3,5,10,22,4,2,7]

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


profit = calculateprofit(price_array)
print(profit)