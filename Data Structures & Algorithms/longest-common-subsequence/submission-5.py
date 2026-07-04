class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS = len(text1)
        COLS = len(text2)

        dp = [[0 for _ in range(COLS+1)] for _ in range(ROWS+1)]

        for row in range(1,ROWS+1):
            for col in range(1,COLS+1):
                val = dp[row-1][col-1]
                if row>0 and col>0 and text1[row-1] == text2[col-1]:
                    val += 1
                dp[row][col] = max(dp[row-1][col], dp[row][col-1], val)

        for row in range(ROWS+1):
            print(dp[row])
        return dp[-1][-1]