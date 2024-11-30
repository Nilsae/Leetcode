class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min = prices[0]
        for price in prices:
            if price < min:
                min = price
            max_profit = max(max_profit, price - min)
        return max_profit
print(Solution().maxProfit(prices = [7,1,5,3,6,4]))