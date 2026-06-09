class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for index_i in range(len(nums)):
            val = nums[index_i]
            if(target-val in hash):
                return [hash[target-val], index_i]
            else:
                hash[val] = index_i
        return[]
        