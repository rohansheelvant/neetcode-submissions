class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while(l <= r):
            mid = (l+r) // 2

            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            elif nums[mid] == target:
                return mid
            elif target > nums[l] and target < nums[mid]:
                r = mid - 1
            elif target > nums[mid] and target < nums[r]:
                l = mid + 1
            else:
                return -1
        
        return -1
        