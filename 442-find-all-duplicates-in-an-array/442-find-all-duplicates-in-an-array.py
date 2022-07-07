class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dnum, res = {}, []
        for i in nums:
            if i in dnum:
                dnum[i] +=1
            else:
                dnum[i] = 1
        for i, j in dnum.items():
            if j>1:
                res.append(i)
        return res