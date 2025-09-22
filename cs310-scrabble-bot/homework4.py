from itertools import chain, combinations


# was initially looking for the list that describes on which days you must buy or sell to find the max profit and i initially thought
# that you didnt have to buy or sell, seems like the solution to this would be finding the maximum element of the 2d power set of 

def stock_profit(prices: list) -> int:
    num = 0
    #find the maximum potential difference for a given range
    i = 1
    for i in range(len(prices)):
        if prices[i] > prices[i - 1]:
            num += prices[i] - prices[i - 1]
    return num