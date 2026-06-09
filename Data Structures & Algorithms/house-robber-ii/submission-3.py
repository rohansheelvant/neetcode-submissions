class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        nums1 = nums[:-1]
        nums2 = nums[1:]

        dp = [0 for val in nums1]
        dp[0] = nums1[0]
        dp[1] = nums1[1]
        for index in range(2, len(nums1)):
            if index-3 >= 0: 
                dp[index] = nums1[index] + max(dp[index-2], dp[index-3])
            else:
                dp[index] = nums1[index] + dp[index-2]
        
        
        dp2 = [0 for val in nums2]
        dp2[0] = nums2[0]
        dp2[1] = nums2[1]
        for index in range(2, len(nums2)):
            if index-3 >= 0: 
                dp2[index] = nums2[index] + max(dp2[index-2], dp2[index-3])
            else:
                dp2[index] = nums2[index] + dp2[index-2]
        
        #print(dp, dp2)
        return max(dp[-2:] + dp2[-2:])