class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_to_reach = [-1] * len(cost)

        # initialize DP
        cost_to_reach[0], cost_to_reach[1] = 0, 0

        for i in range(2, len(cost)):
            cost_to_reach[i] = min(cost_to_reach[i-1]+cost[i-1], 
            cost_to_reach[i-2]+cost[i-2])
        
        return min(cost_to_reach[-1]+cost[-1], cost_to_reach[-2]+cost[-2])


        