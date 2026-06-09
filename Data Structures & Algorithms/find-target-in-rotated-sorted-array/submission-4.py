class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)
        
        def loop(l, r):
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if r-l == 1:
                if nums[l] == target:
                    return l
                elif nums[r] == target:
                    return r
                else:
                    return -1
            else:
                mid = (l+r) // 2
                
                if nums[mid] > nums[l]:
                    if target >= nums[mid]:
                        return loop(mid, r)
                    elif target >= nums[l]:
                        return loop(l, mid)
                    else:
                        return loop(mid, r)
                else:
                    if target >= nums[l]:
                        return loop(l, mid)
                    elif target >= nums[mid]:
                        return loop(mid, r)
                    else:
                        return loop(l, mid)
        
        if nums_len == 0:
            return -1
        elif nums_len == 1:
            return 0 if target == nums[0] else -1
        else:
            return loop(0, nums_len-1)
            
        