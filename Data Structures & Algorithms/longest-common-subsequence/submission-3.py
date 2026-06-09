class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * len(text2)
        for val in text1:
            max_so_far = 0
            for index in range(0, len(text2)):
                if text2[index] == val:
                    max_curr = max(dp[index],max_so_far)
                    dp[index] = max(max_so_far+1, dp[index])
                    max_so_far = max_curr
                else:
                    max_so_far = max(max_so_far, dp[index])
        
        return max(dp)
                

        