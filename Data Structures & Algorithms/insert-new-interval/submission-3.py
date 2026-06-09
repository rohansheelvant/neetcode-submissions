class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        return_list = []

        if intervals == []:
            return [newInterval]

        s1, e1 = newInterval
        index = 0
        added = False
        while(index < len(intervals)):
            start, end = intervals[index]
            if s1 > end or e1 < start:
                if e1 < start and not added:
                    return_list.append([s1,e1])
                    added = True
                return_list.append([start,end])
                index += 1
            else:
                s2 = min(s1, start)
                while(start <= e1 and index < len(intervals)):
                    e2 = max(e1, end)
                    index += 1
                    if index < len(intervals):
                        start, end = intervals[index]
                return_list.append([s2,e2])
                added = True
        
        if not added:
            return_list.append([s1,e1])

        return return_list