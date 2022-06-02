from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            dic[i] = 1 + dic.get(i, 0)
            
        freq = defaultdict(list)
        for num, val in dic.items():
            freq[val].append(num)
            
        freqs = list(freq.keys())
        freqs.sort()
        output = []
        while len(output)<k:
            f = freqs.pop()
            output.extend(freq[f])
            
        return output
            
        
        
        
       