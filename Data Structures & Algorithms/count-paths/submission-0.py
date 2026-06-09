class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)]] * m

        # Initialize 
        for index in range(len(dp[0])):
            dp[0][index] = 1
        for index in range(len(dp)):
            dp[index][0] = 1
        
        for row in range(1, m):
            for column in range(1, n):
                dp[row][column] = dp[row-1][column] + dp[row][column-1]
        
        return dp[-1][-1]

        