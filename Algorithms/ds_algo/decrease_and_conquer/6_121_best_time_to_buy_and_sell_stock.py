


# 121. Best Time to Buy and Sell Stock
#
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.


class Solution:
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        global_max = 0
        leastprice = prices[0]
        for i in range(1, len(prices)):
            if prices[i] - leastprice > global_max:
                global_max = prices[i] - leastprice
            leastprice = min(leastprice, prices[i])
        return global_max


# OR

class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) == 0:
            return 0
        global_max = 0
        leastprice = prices[0]
        for i in range(1, len(prices)):
            global_max = max(global_max,  prices[i] - leastprice)
            leastprice = min(leastprice, prices[i])
        return global_max

# OR

class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) == 0:
            return 0
        global_max = 0
        leastprice = prices[0]
        for i in range(1, len(prices)):
            leastprice = min(leastprice, prices[i])
            global_max = max(global_max,  prices[i] - leastprice)
        return global_max

# OR
class Solution:
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        global_max = 0
        leastprice = prices[0]
        for i in range(1, len(prices)):
            leastprice = min(leastprice, prices[i])
            if prices[i] - leastprice > global_max:
                global_max = prices[i] - leastprice
        return global_max

