import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distance: list(tuple(float, list[int, int])) = []

        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            distance.append((dist, point))
        
        distance.sort(key=lambda x:x[0])

        return [p for d,p in distance][:k]
        