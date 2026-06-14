class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total%2 != 0:
            return False
        
        half_sum = [False] * (int(total//2)+1)
        len_hs = len(half_sum)

        for num in nums:
            indices = [i for i, val in enumerate(half_sum) if val]
            for index in indices:
                if half_sum[index] and index+num < len_hs:
                    half_sum[index+num] = True
                
            if num < len_hs:
                half_sum[num] = True        

        return half_sum[-1]
        