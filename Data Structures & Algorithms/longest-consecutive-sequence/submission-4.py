class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        track = {}

        for val in nums:
            track[val] = 1
        
        for val in nums:
            if track[val] != 1:
                continue
            
            while(val-1 in track):
                val = val-1
            
            while(val+1 in track):
                val = val + 1
                track[val] = track[val-1]+1
        
        return max(track.values()) if track else 0
            
        
