class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        max_so_far = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            if prices[i] <= max_so_far:
                max_profit = max(max_profit, max_so_far-prices[i])
            else:
                max_so_far = max(max_so_far, prices[i])
        
        return max_profit


        