class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_val = nums[0]
        dp_max = nums[0]
        dp_min = nums[0]
        for index in range(1, len(nums)):
            dp_max, dp_min = max(nums[index], dp_max*nums[index], dp_min*nums[index]), min(nums[index], dp_max*nums[index], dp_min*nums[index])
            max_val = max(max_val, dp_max)

        return max_val
        


        