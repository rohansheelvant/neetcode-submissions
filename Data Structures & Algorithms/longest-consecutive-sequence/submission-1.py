class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        set_val = set(nums)
        visited = []
        max_len = 1

        for val in nums:
            if val in visited:
                continue
            visited.append(val)
            length = 1
            curr_val = val
            while(curr_val+1 in set_val):
                length += 1
                curr_val += 1
                visited.append(curr_val)
            
            max_len = max(max_len, length)
        
        return max_len
            
            


    