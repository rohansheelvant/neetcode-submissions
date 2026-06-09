class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = max(nums)
        total = None
        for val in nums:
            if total == None:
                total = val
            else:
                total = max(val, val+total)
            max_sum = max(max_sum, total)
        return max_sum