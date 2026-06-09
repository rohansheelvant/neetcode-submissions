class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k, max_k = 1, max(piles)

        def findHours(k):
            hours = 0
            for val in piles:
                if val % k == 0:
                    hours += val / k
                else:
                    hours += (val//k) + 1
            return hours

        op = -1
        while(min_k<=max_k):
            mid_k = (min_k+max_k) // 2
            hours = findHours(mid_k)
            if hours > h:
                min_k = mid_k+1
            else:
                op = mid_k
                max_k = mid_k-1
        return op

        

        