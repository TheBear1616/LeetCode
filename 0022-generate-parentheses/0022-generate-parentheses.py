class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(curr, openBrak, closeBrak):
            if openBrak == closeBrak == n:
                result.append(curr)
                return
            
            if openBrak < n:
                backtrack(curr + "(", openBrak + 1, closeBrak)

            
            if closeBrak < openBrak:
                backtrack(curr + ")", openBrak, closeBrak + 1)
        

        backtrack("", 0, 0)    
        return result
