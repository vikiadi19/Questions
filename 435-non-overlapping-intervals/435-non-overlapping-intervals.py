class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i: i[0])
        
        res = [intervals[0]]
        for i in intervals:
            if res[-1][1] > i[0]:
                if res[-1][1] > i[1]:
                    res.pop(-1)
                    res.append(i)
                else:
                    continue
            else:
                res.append(i)
                    
        return len(intervals)-len(res)