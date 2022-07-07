class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        sset = set()
        maxL = 0
        while r<len(s):
            if s[r] not in sset:
                sset.add(s[r])
                r+=1
            else:
                sset.remove(s[l])
                l+=1
            maxL = max(len(sset), maxL)
            
        return maxL
        
