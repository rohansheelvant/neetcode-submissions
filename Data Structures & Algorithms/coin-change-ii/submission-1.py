class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [0] * (amount+1)

        dp_len = len(dp)
        dp[0] = 1
        for coin in coins:
            if coin < dp_len:
                dp[coin] += 1
            for i in range(1, dp_len):
                if dp[i] != 0 and i+coin < dp_len:
                    dp[i+coin] += dp[i]
                
        return dp[-1]

        