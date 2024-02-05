class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def backtrack(openedP, closedP):
            if openedP == closedP == n:
                result.append("".join(stack))
                return 
            
            if openedP < n:
                stack.append("(")
                backtrack(openedP + 1, closedP)
                stack.pop()

            if closedP < openedP:
                stack.append(")")
                backtrack(openedP, closedP + 1)
                stack.pop()

        backtrack(0,0)
        return result