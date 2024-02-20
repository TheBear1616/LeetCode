class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phNumDict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []
        if len(digits) == 0:
            return result

        def backtrack(idx, curr):
            if len(curr) == len(digits):
                result.append(curr)
                return
            
            if idx >= len(digits):
                return
            
            for char in phNumDict[digits[idx]]:
                backtrack(idx + 1, curr + char)        

        backtrack(0, "")
        return result