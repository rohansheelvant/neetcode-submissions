class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums) 
        if total_sum % 2 != 0:
            return False
        
        dp = [False] * ((total_sum//2)+1)
        dp[0] = True

        for val in nums:
            for i in range(len(dp)-1, -1, -1):
                if i - val >=0 and dp[i-val]:
                    dp[i] = True
        
        return dp[-1]