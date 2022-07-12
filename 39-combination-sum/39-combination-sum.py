class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # if target<0:
        #     return []
        # if target == 0:
        #     return [[]]
        # res = []
        # for i in range(len(candidates)):
        #     combos = self.combinationSum(candidates[i:], target-candidates[i])
        #     if type(combos) == list:
        #         for combo in combos:
        #             combo.append(candidates[i])
        #             res.append(combo)
        #         # print(res)
        # return res




        res = []
        def lno(candidates, target, asf):
            if target<0:
                return 
            if target==0:
                res.append(asf.copy())
                # asf.clear()
                return

            for i in range(len(candidates)):
                asf.append(candidates[i])
                lno(candidates[i:], target-candidates[i], asf)   
                asf.pop()
                
        asf = []
        lno(candidates, target, asf)   
        return res