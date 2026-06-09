class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        op = []
        len_nums = len(nums)

        def loop(start_index, target):
            op_ret = []
            for i in range(start_index, len_nums):
                if target == nums[i]:
                    op_ret.append([nums[i]])
                elif target == 0:
                    return [[]]

                elif target - nums[i] > 0:
                    ret_vals = loop(i, target - nums[i])
                    for rets in ret_vals :
                        ret = [nums[i]] + rets
                        op_ret.append(ret)
            
            return op_ret

        for index in range(0, len(nums)):
            ret_list = loop(index, target-nums[index])
            for sub_list in ret_list:
                op.append([nums[index]] + sub_list)
        
        return op
        
        



        