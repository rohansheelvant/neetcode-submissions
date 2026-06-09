class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key= lambda x: (x[0], x[1]) )

        if intervals == []:
            return intervals

        output = []
        curr_s, curr_e = intervals[0][0], intervals[0][1]
        index = 1
        while(index < len(intervals)):
            new_s, new_e = intervals[index]
            if new_s > curr_e:
                output.append([curr_s, curr_e])
                curr_s, curr_e = new_s, new_e
            
            else:
                curr_s = min(curr_s, new_s)
                curr_e = max(curr_e, new_e)

            index += 1
        output.append([curr_s, curr_e])
        return output



