class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {} # {value:index}
        for i in range(len(nums)):
            if target-nums[i] in d:
                return [i, d[target-nums[i]]]
            else:
                d[nums[i]] = i
                
                
                
            