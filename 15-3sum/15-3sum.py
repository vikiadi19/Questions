class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            
        # targetset = set()
        nums.sort()
        res = set()
        for i in range(len(nums)):
            if i != 0 and nums[i-1] == nums[i]:
                pass
                
            else:
                target = -nums[i]
                self.sum2(nums[:i]+nums[i+1:], target, res)
                    
        return res
    
    def sum2(self, nums, target, reso):
            l, h = 0, len(nums)-1
            ans = []
            while l<h:
                summ = nums[l] + nums[h]
                if summ > target:
                    h-=1
                elif summ < target:
                    l+=1
                else:
                    ans = [-target, nums[l], nums[h]]
                    ans.sort()
                    reso.add(tuple(ans))
                    l += 1
                    h -= 1
        
        