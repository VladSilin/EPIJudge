from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    if not prices:
        return 0
    elif len(prices) == 1:
        return 0

    # [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    buy = prices[0]
    sell = prices[1]

    profit = max(0.0, sell - buy)

    j = 1
    while j < len(prices):
        if prices[j] < buy:
            buy = prices[j]
        else:
            if prices[j] - buy > profit:
                profit = max(0.0, prices[j] - buy)

        j += 1

    return profit


# Input:

# Output:

# Notes / Assumptions:

# Example:
# A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
#                                         l
# h = 30
def buy_and_sell_stock_once_attempt2(prices: List[float]) -> float:
    low = prices[0]
    highest_profit = 0
    for i in range(1, len(prices)):
        delta = prices[i] - low
        highest_profit = max(delta, highest_profit)
        low = min(low, prices[i])

    return highest_profit


if __name__ == '__main__':
    #input = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

    #result = buy_and_sell_stock_once_attempt2(input)

    #print(result)

    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
