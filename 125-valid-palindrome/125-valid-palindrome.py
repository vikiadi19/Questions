class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        
        while left < right:
            
            if s[left].isalnum() and s[right].isalnum():
                ls, rs = s[left].lower(), s[right].lower()
                if ls==rs:
                    left = left + 1
                    right = right-1
                else:
                    return False
                
            if not s[left].isalnum():
                left=left+1
            if not s[right].isalnum():
                right=right-1 
                
        return True
                    
        
            
                