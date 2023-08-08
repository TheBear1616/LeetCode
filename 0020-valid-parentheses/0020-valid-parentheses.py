class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '{':'}','[':']'}
        stack = []
        for brak in s:
            if brak in brackets:
                stack.append(brak)
            elif len(stack) == 0 or brak != brackets[stack.pop()]:
                return False
        
        return len(stack) == 0