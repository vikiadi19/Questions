class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        op = []
        for i in nums:
            idx = abs(i)-1
            if nums[idx] < 0:
                op.append(abs(i))
            nums[idx] *= -1
        return op