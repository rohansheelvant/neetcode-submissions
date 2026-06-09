class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)

        #initialize 
        for index in coins:
            if index<=amount:
                dp[index] = 1
        dp[0] = 0

        # Fill dp
        for val in range(1, amount+1):
            for coin_val in coins:
                if val-coin_val >=0:
                    dp[val] = min(dp[val], 1+dp[val-coin_val])
        
        return -1 if dp[-1]==float('inf') else dp[-1]
        