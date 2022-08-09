from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d, op = {}, []
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        d2 = {}
        for key, value in d.items():
            if value not in d2:
                d2[value] = [key]
            else:
                d2[value].append(key)
                
        while len(op)<k:   
            maxi = max(d2.keys())
            op.extend(d2[maxi])
            del d2[maxi]
            
        return op
            

        
        
        
       