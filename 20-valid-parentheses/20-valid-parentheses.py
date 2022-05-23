from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        # chars = {"(":")", "[":"]", "{":"}"}
        chars = {")":"(", "]":"[", "}":"{"}
        stack = []
        # stack.append(s[0])
        for i in s:
            stack.append(i)
            if stack[-1] in chars.values():
                pass
            
            elif len(stack)>1 and chars[stack[-1]] == stack[-2]:
                stack.pop()
                stack.pop()
            else:
                return False
            
        if len(stack) == 0:
            return True
            
            # stack.append(i):