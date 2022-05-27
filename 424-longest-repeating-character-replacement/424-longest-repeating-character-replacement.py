class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # d, changes_allowed, maxL = {}, k, 0
        # for i in range(len(s)):
        #     d[s[i]] = 1 + d.get(s[i], 0)
        # max_key = max(d, key=d.get)
        l, r, res = 0, 0, 0
        count = {}
        while r<len(s):
            count[s[r]] = 1 + count.get(s[r],0)
            
            if (r-l+1)-max(count.values())>k:
                count[s[l]]-=1
                l+=1
            
            res = max(res, r-l+1)
            r+=1
        return res