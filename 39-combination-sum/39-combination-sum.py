class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target<0:
            return []
        if target == 0:
            return [[]]
        res = []
        for i in range(len(candidates)):
            combos = self.combinationSum(candidates[i:], target-candidates[i])
            if type(combos) == list:
                for combo in combos:
                    combo.append(candidates[i])
                    res.append(combo)
                # print(res)
        return res




# res = []
#         def lno(candidates, target, asf):
#             if target<0:
#                 return 
#             if target==0:
#                 res.append(asf)
#                 return
            
#             for i in candidates:
#                 lno(candidates, target-i, asf.append(i))
                
#         lno(candidates, target, [])   
#         return res