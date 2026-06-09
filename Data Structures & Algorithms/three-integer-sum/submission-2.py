class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        op = set()

        for j in range(1, len(nums)-1):
            i = j - 1
            k = j + 1
            while(i>=0 and k<len(nums)):
                if nums[i] + nums[k] + nums[j] == 0:
                    while(i-1 >=0 and nums[i-1] == nums[i]):
                        i -= 1
                    while(k+1 <len(nums) and nums[k+1] == nums[k]):
                        k += 1

                    if (nums[i],nums[j],nums[k]) not in op: 
                        op.add((nums[i],nums[j],nums[k]))

                    i -= 1
                    k += 1
                
                elif nums[i] + nums[k] + nums[j] > 0:
                    i -= 1
                elif nums[i] + nums[k] + nums[j] < 0:
                    k += 1
        op = [list(val) for val in op]
        return op

