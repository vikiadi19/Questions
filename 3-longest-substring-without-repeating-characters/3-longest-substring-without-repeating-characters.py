class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        if s == "":
            maxL = 0
        else:
            maxL = 1
        while r<len(s):
            if len(s[l:r+1]) == len(set(s[l:r+1])):
                length = r-l+1
                maxL = max(maxL, length)
            else:
                l +=1
            r += 1
            
        return maxL