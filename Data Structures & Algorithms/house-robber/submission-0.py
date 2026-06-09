class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        dp = [0 for val in nums]
        dp[0] = nums[0]
        dp[1] = nums[1]
        for index in range(2, len(nums)):
            if index-3 >= 0: 
                dp[index] = nums[index] + max(dp[index-2], dp[index-3])
            else:
                dp[index] = nums[index] + dp[index-2]
        
        return max(dp[-2:])
        
        