from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i]  = 1
            else:
                dic[i] += 1
        
        d = {}
        for i in dic.keys():
            if dic[i] not in d:
                d[dic[i]] = [i]
            else:
                d[dic[i]].append(i)
        l = []
        for i in d.keys():
            l.append(i)
            
        l.sort()
        fin = []
        while len(fin)<k:
            x = l.pop()
            fin.extend(d[x])
            
        return (fin)