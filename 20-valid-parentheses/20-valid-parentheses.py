from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        stack = []
        d = {")":"(", "}":"{", "]":"["}
        for i in s:
            if i in d.values():
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if d[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
                    
        return len(stack) == 0
            