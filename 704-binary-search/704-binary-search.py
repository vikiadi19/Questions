class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res, rem = 0, 0
        while len(nums)>1:
            midpt = len(nums)//2
            if nums[midpt] == target:
                res = midpt + rem
                break
            elif nums[midpt] > target:
                nums[:] = nums[:midpt]
                # rem += midpt
            else:
                nums[:] = nums[midpt:]
                rem += midpt
        if len(nums) == 1 and nums[-1] == target:
            return 0
            
        if res != 0:
            return res
        return -1