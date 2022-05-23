class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # lis = [[for i in nums] for j in range(len(nums))]
        # for i in range(lis):
        prod1, prod2, count = 1, 1, 0
        for i in nums:
            prod1 *= i
            if i != 0:
                prod2 *= i
            else:
                count += 1
            
            
        fin = [1]*len(nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                fin[i] = prod1//nums[i]
            else:
                if count > 1:
                    fin[i] = 0
                else:
                    fin[i] = prod2
        return fin