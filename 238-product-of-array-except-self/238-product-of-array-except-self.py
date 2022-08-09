class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_prod = 1
        op, d = [], {}
        for i in nums:
            if i != 0:
                all_prod *= i
            d[i] = 1+d.get(i, 0)
            
        if 0 in d and d[0] > 1:
            op = [0]*len(nums)
        elif 0 in d and d[0] == 1:
            for i in nums:
                if i == 0:
                    op.append(all_prod)
                else:
                    op.append(0)
        else:
            for i in nums:
                op.append(all_prod//i)
                
        return op
            

