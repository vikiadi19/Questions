from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i]  = 1
            else:
                dic[i] += 1
        
        d = defaultdict(list)
        for i in dic.keys():
            d[dic[i]].append(i)
            
        fin = []
        while len(fin)<k:
            fin.extend(d[max(d.keys())])
            del d[max(d.keys())]
            
        return (fin)
        
        
       