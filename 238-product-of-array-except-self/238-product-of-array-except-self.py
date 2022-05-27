class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix, p = [0]*len(nums), [0]*len(nums), 1
        for i in range(len(nums)):
            if i == 0:
                p = 1
            else:
                p = p * nums[i-1]
            prefix[i] = p
            
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                p = 1
            else:
                p = p * nums[i+1]
            postfix[i] = p
            
        # print(prefix, postfix)
        res = []
        for i in range(len(nums)):
            res.append(postfix[i]*prefix[i])
            
        return res