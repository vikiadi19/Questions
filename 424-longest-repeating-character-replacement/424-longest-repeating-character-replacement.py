class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # d, changes_allowed, maxL = {}, k, 0
        # for i in range(len(s)):
        #     d[s[i]] = 1 + d.get(s[i], 0)
        # max_key = max(d, key=d.get)
        d = {}
        l, maxL = 0, 0
        for r in range(len(s)):
            d[s[r]] = 1 + d.get(s[r], 0) 
            while (r-l+1)-max(d.values())>k:
                d[s[l]] -= 1
                l += 1
            maxL = max(maxL, r-l+1)
        return maxL
            