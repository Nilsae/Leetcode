class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        left = 0
        right = 1
        cur_val = 0
        profit = 0
        while right < n:
            if prices[right] - prices[left] > cur_val:
                print(f'buy:', left, "sell", right)
                cur_val = prices[right] - prices[left]
                profit = profit + cur_val
                right = right + 1
                right = left + 1
                curr_val = 0
            if prices[right] - prices[left] < 0:
                # cur_val = 0
                left = right + 1
                right = left + 1
          
        return profit
    
print(Solution().maxProfit(prices = [7,1 ,5,3,6,4]))