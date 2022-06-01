class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                return True
            
        return False
    
    
    
    #sol1 - compare set(nums) to nums, if there is difference in length then True
        #TC - O(n), SC - O(n)
    #sol2 - create a dictionary or frequency distribution - any element if has value greater than 1, break and return true or that key
        #TC - O(n), SC - O(n)
    #sol3 - sort and use two pointers side by side, if both pointers point to same value then return True and return that value.
        #TC - O(nlogn), SC-O(1)
    
    
    