class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return min(nums)
    
        def loop(l, r):
            if r-l == 1:
                return min(nums[l:r+1])
            mid = (r+l) // 2
            if nums[mid] > nums[r]:
                return loop(mid, r)
            else:
                return loop(l, mid)
        
        return loop(0, len(nums)-1)
        