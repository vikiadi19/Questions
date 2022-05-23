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
            
        # l.sort()
        fin = []
        for i in range(len(nums), -1, -1):
            
            if len(fin)<k:
                if i in d:
                    fin.extend(d[i])
            else:
                return fin
                    

        return (fin)