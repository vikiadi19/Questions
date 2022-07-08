class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ""
        for i in s:
            if i.isalnum():
                s_new+= i.lower()
        
        return s_new == s_new[::-1]
            