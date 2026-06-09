class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

        hm = defaultdict(int)

        for val in nums:
            hm[val] += 1
        
        hm1 = defaultdict(list)
        for key, value in hm.items():
            hm1[value].append(key)
        
        max_val = max(hm1.keys())
        
        total = 0
        op = []
        for i in range(max_val, -1, -1):
            if hm1[i] != []:
                total += len(hm1[i])
                op += hm1[i]
            if total == k:
                return op