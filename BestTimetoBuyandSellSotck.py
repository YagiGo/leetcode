"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#The dumb way, O(n^2). Time Limitation exceeds
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        maxProfit = 0
        for i in range(len(prices)):
            j = 0
            while j < i:
                profit = prices[i] - prices[j]
                if profit > maxProfit:
                    maxProfit = profit
                j += 1
        return maxProfit
    # now this exceeds time limitation
        """
        """
        maxProfit = 0
        for i in range(len(prices)):
            highestPrice = max(prices[i:])
            if prices[i] < highestPrice and maxProfit < highestPrice-prices[i]:
                maxProfit = highestPrice-prices[i]
        return maxProfit
        # This also exceeds time limitation
        """
    # Find the maxDiff, and this is it
        if len(prices) == 0 or len(prices) == 1:
            return 0
        minPrice = prices[0]
        maxProfit = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            elif maxProfit < price - minPrice:
                maxProfit = price - minPrice
        return maxProfit
        
