class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1= {}
        if len(s)!=len(t):
            return False
        else:
            for i in range(len(s)):
                d1[s[i]] = 1 + d1.get(s[i], 0)
            
            for j in range(len(t)):
                if t[j] not in d1:
                    return False
                else:
                    d1[t[j]] -= 1
                    
            for val in d1.values():
                if val!=0:
                    return False
        
            return True