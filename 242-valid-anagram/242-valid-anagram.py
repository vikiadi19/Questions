class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        for i in s:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        for l in t:
            if l in d1:
                d1[l] -= 1
            else:
                return False
        if any(d1.values()):
            return False
        
        return True