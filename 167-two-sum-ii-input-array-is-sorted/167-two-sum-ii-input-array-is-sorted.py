class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers)-1
        while low<high:
            summ = numbers[low]+numbers[high]
            if summ < target:
                low += 1
            elif summ > target:
                high -= 1
            else:
                return [low+1, high+1]
            
        # left, right = 0, len(numbers)-1
        # while left<=right:
        #     if numbers[left] + numbers[right] > target:
        #         right -= 1
        #     elif numbers[left] + numbers[right] < target:
        #         left += 1
        #     else:
        #         return [left+1, right+1]