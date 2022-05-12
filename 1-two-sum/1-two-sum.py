class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if target - nums[i] not in d.keys():
                d[nums[i]] = i
            else:
                return [i, d[target-nums[i]] ]
                
                
                
    # {2:0, 2:1, }