class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        possible = [False, False, False]

        for trip in triplets:
            if trip[0] == target[0] and trip[1] <= target[1] and trip[2] <= target[2]:
                possible[0] = True
            if trip[1] == target[1] and trip[0] <= target[0] and trip[2] <= target[2]:
                possible[1] = True
            if trip[2] == target[2] and trip[1] <= target[1] and trip[0] <= target[0]:
                possible[2] = True
        
        return all(possible)
            
