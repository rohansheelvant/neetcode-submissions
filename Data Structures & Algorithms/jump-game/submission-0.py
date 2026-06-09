class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_dist = 0
        for index_i, val in enumerate(nums):
            if index_i > max_dist:
                return False
            max_dist = max(max_dist, index_i+val)
        return True
