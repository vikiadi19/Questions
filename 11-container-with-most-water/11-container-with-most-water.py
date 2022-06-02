class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_area = min(height[l],height[r])*(r-l)
        while l<r:
            if height[l]<height[r]:
                l = l+1
            else:
                r = r-1
            area = min(height[l],height[r])*(r-l)
            max_area = max(area, max_area)
            
        return max_area