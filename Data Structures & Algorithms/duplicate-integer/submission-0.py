class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        track = set()
        for val in nums:
            if val not in track:
                track.add(val)
            else:
                return True

        return False
        