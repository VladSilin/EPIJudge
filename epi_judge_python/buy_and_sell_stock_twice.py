from typing import List

from test_framework import generic_test
import heapq

# Input:
# - prices: List[float], list of prices of a single stock

# Output:
# - highest_profit: float, highest profit buying + selling the stock twice

# Notes / Assumptions:
# - Second buy must be after first one's SALE

# Example:
# A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
#                                         l1
#                               l2
#                                                  i
#
# profit1 = 30
# profit2 = 20
def buy_and_sell_stock_twice0(prices: List[float]) -> float:
    lowest = prices[0]
    profit = 0
    last_highest_profit = 0
    h = []

    i = 1
    while i < len(prices):
        #profit = max(prices[i] - lowest, profit)

        delta = prices[i] - lowest
        if delta > profit:
            profit = delta
            last_highest_profit = i

        # TODO: Store WHERE you found the highest profit, "resume" the index from there
        if prices[i] < lowest:
            lowest = prices[i]
            heapq.heappush(h, profit)
            profit = 0
        elif i == len(prices) - 1:
            heapq.heappush(h, profit)

        i += 1

    # TODO: Return value
    return sum(heapq.nlargest(2, h))


# Example:
# A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
def buy_and_sell_stock_twice(prices: List[float]) -> float:
    if not prices:
        return 0

    # Compute max profit up to and including price i
    profits_forward = [0]
    low_f = prices[0]
    profit_f = 0
    for i in range(1, len(prices)):
        delta = prices[i] - low_f
        profit_f = max(profit_f, delta)
        profits_forward.append(profit_f)
        low_f = min(low_f, prices[i])

    # Compute profits if allowed last allowed "2nd buy" date is j
    # (Note that this list will be reversed since we are appending to profits_backward)
    profits_backward = [0]
    high_b = prices[len(prices) - 1]
    profit_b = 0

    # Start from the second-last element
    for j in range(len(prices) - 2, -1, -1):
        delta = high_b - prices[j]
        profit_b = max(profit_b, delta)
        profits_backward.append(profit_b)
        high_b = max(high_b, prices[j])

    profits_backward.reverse()

    max_profit = float('-inf')
    for k in range(len(prices)):
        f_value = profits_forward[k - 1] if k - 1 > -1 else 0
        profit = f_value + profits_backward[k]
        max_profit = max(profit, max_profit)

    return max_profit

if __name__ == '__main__':
    #input = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    #input = [0.7, 12.7, 0.4, 0.9, 8.7, 12.3, 1.4, 0.1, 0.8, 8.9, 13.6, 6.5, 9.6, 6.3, 11.7, 6.9, 7.2, 11.9, 3.1, 0.4, 10.9, 2.8, 9.8, 13.6, 12.5, 6.9, 12.4, 7.0, 1.6, 1.5, 8.4, 1.2, 9.1, 9.8, 5.2, 3.8, 1.3, 7.9, 8.1, 3.4, 2.3, 9.3, 4.5, 1.0, 11.9, 3.6, 4.9, 10.5, 4.7, 10.6, 3.4, 6.4, 7.9, 8.3, 8.0, 10.0, 6.4, 11.6, 2.5, 4.1, 8.7, 5.0, 4.7, 6.9, 6.1]

    #result = buy_and_sell_stock_twice(input)

    #print(result)

    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
