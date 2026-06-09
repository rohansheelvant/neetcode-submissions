class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        len_dp = [1] * len(nums)
        for index in range(0, len(nums)):
            for back_index in range(index-1, -1, -1):
                if nums[back_index] < nums[index]:
                    len_dp[index] = max(len_dp[index], len_dp[back_index]+1)
        
        return max(len_dp)
                

        