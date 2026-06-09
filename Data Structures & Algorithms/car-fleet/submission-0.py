class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        time = [ (target - position[i])/speed[i] for i in range(len(speed)) ]

        position, time = zip(*sorted(zip(position, time)))

        groups = []
        for val in time:
            if groups == []:
                groups.append(val)
            else:
                if val < groups[-1]:
                    groups.append(val)
                else:
                    while(groups and val >= groups[-1]):
                        groups.pop()
                    
                    groups.append(val)
        
        return len(groups)




        