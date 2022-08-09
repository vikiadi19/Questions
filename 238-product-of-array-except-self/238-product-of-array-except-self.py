class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op = []
        prod = 1
        for i in range(len(nums)):
            if i == 0:
                prod = 1
            else:
                prod *= nums[i-1]
            op.append(prod)
            
        prod = 1   
        # op = op[::-1]
        for i in range(len(nums)-1, -1, -1):
            if i+1 > len(nums)-1:
                prod = 1
            else:
                prod *= nums[i+1]
            op[i] *= prod

        # op = []
        # post = post[::-1]
        # for i in range(len(nums)):
        #     op.append(pre[i]*post[i])
            
        return op

