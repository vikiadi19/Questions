class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h, n = 0, len(nums)-1, len(nums)
        while l<=h:
            mid = l + (h-l)//2
            nex = (mid+1)%n
            prev = (mid+n-1)%n
            
            if nums[l]<=nums[h]:
                return nums[l]
            
            elif nums[mid]<nums[prev] and nums[mid]<nums[nex]:
                return nums[mid]
            
            elif nums[mid]<=nums[h]:
                #lie on left side, update high
                h = mid-1
                
            elif nums[l]<=nums[mid]:
                #lie on the right side, update low
                l = mid + 1
                
        return -1