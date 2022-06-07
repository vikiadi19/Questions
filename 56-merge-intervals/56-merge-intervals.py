class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])
        if len(intervals)==1:
            return intervals
        res = [intervals[0]]
        for i in range(len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
                res[-1][0] = min(res[-1][0], intervals[i][0])
            else:
                res.append(intervals[i])
                
        return res