class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros_count = nums.count(0)
        if zeros_count >= 2:
            return [0 for _ in nums]
        elif zeros_count == 1:
            product = 1
            for val in nums:
                if val:
                    product *= val
            
            index = nums.index(0)

            return [0 if key != index else product for key, _ in enumerate(nums)]
        else:
            product = 1
            for val in nums:
                product *= val
            
            return [int(product/val) for val in nums]
        
        