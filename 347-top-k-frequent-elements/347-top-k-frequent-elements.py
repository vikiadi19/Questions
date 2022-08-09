from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d, op = {}, []
        for i in nums:
            d[i] = 1 + d.get(i, 0)
        d2 = defaultdict(list)
        for key, value in d.items():
            d2[value].append(key)
                
        while len(op)<k:   
            maxi = max(d2.keys())
            op.extend(d2[maxi])
            del d2[maxi]
            
        return op
            

        
        
        
       