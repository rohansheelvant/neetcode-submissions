class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr_index = 0
        start_index = 0

        net_fuel_remaining = 0
        loop_completed = False

        while(start_index <= len(gas)-1):
            if curr_index == start_index and loop_completed:
                if net_fuel_remaining >= 0:
                    return curr_index
                else:
                    return -1
            
            net_fuel_remaining += (gas[curr_index]-cost[curr_index])
            curr_index += 1
            if curr_index == len(gas):
                loop_completed = True
            curr_index = curr_index % len(gas)
            if net_fuel_remaining < 0:
                print(start_index, loop_completed, curr_index)
                if curr_index <= start_index:
                    return -1
                net_fuel_remaining = 0
                start_index = curr_index

        return -1