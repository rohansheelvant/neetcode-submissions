class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        def loop(nums_list, curr_list):
            if nums_list == []:
                return
            for i in range(0, len(nums_list)):
                temp = curr_list + [nums_list[i]]
                output.append(temp)
                loop(nums_list[i+1:], temp)
        loop(nums, [])
        return output
