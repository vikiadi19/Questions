class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n-1
        while low<=high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<=nums[high]:
                #mid to high are sorted
                if target>=nums[mid] and target<=nums[high]:
                    low = mid+1
                else:
                    high = mid-1
                    
                    
            elif nums[low]<=nums[mid]:
                #low to mid are sorted
                if target>=nums[low] and target<=nums[mid]:
                    high = mid - 1
                else:
                    low = mid+1
                    
        return -1