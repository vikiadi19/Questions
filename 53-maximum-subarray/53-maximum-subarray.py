class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = 0
        maxSub = nums[0]
        for i in nums:
            if cursum < 0:
                cursum = 0
            cursum += i
            maxSub = max(maxSub, cursum)
            
        return maxSub