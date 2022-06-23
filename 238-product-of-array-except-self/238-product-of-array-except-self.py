class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op = [0]*len(nums)
        prod = 1
        for i in range(len(nums)):
            if i-1<0:
                p = 1
            else:
                p = nums[i-1]
            op[i] = p * prod
            prod = p * prod
        
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            if i+1 > len(nums)-1:
                p = 1
            else:
                p = nums[i+1]
        #     print(prod)
            op[i] *= p*prod
            prod *= p
        
        return op
    

