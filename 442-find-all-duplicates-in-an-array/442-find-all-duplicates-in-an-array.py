class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d, op, i = {}, [], 0
        while len(nums)>0:
            if nums[i] not in d.keys():
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
            nums.pop(i)
        
        for i in d.keys():
            if d[i] > 1:
                op.append(i)
                
        return op
                