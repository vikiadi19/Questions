class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # i = 0
        # while (intervals[i][0] < newInterval[0]) and i<len(intervals):
        #     i+=1
        # if intervals[i+1][0] < newInterval[1]:
        #     intervals.insert(newInterval, i)
        op = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                op.append(newInterval)
                return op + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                op.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                
        op.append(newInterval)
        return op
                