class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        set_val = set(nums)
        max_len = 1

        for val in set_val:
            if val-1 in set_val:
                continue
            length = 1
            curr_val = val
            while(curr_val+1 in set_val):
                length += 1
                curr_val += 1
            
            max_len = max(max_len, length)
        
        return max_len
            
            


    