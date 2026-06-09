"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        end_times = []
        intervals = sorted(intervals, key= lambda x:x.start)
        
        for interval in intervals:
            if end_times == []:
                end_times.append(interval.end)
                continue
            
            start, end = interval.start, interval.end

            added = False
            for index in range(len(end_times)):
                if start >= end_times[index]:
                    end_times[index] = end
                    added = True
                    break
            if not added:
                end_times.append(end)
        
        print(end_times)
        return len(end_times)
        