class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodAll, op, flag, count = 1, [], False, 0
        for i in nums:
            if i!= 0:
                prodAll *= i
            if i == 0:
                flag = True
                count += 1
            
        for i in nums:
            if count >1:
                op.append(0)
            else:
                if flag == True:
                    if i == 0:
                        op.append(prodAll)
                    else:
                        op.append(0)
                else:
                    op.append(prodAll//i)

        return op