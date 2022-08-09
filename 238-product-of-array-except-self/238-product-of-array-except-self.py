class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = [], []
        prod = 1
        for i in range(len(nums)):
            if i == 0:
                prod = 1
            else:
                prod *= nums[i-1]
            pre.append(prod)
            
        prod = 1    
        for i in range(len(nums)-1, -1, -1):
            if i+1 > len(nums)-1:
                prod = 1
            else:
                prod *= nums[i+1]
            post.append(prod)

        op = []
        post = post[::-1]
        for i in range(len(nums)):
            op.append(pre[i]*post[i])
            
        return op

