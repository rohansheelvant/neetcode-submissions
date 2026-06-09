import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)
        print(max_heap)

        while(max_heap and len(max_heap) > 1):
            w1 = -heapq.heappop(max_heap)
            w2 = -heapq.heappop(max_heap)
            if w1!=w2:
                heapq.heappush(max_heap, -abs(w1-w2))
        
        return -max_heap[0] if max_heap else 0