class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        strset = set()
        l= r = 0
        
        # length = 0
        while r<len(s):
            if s[r] not in strset:
                strset.add(s[r])
                r+=1
            else:
                maxL = max(maxL, len(strset))
                # length = 0
                strset.clear()
                l += 1
                r = l
            # print(strset)
        maxL = max(maxL, len(strset))
        return maxL
