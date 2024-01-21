class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        combination = []

        def backtrack(num):
            if len(combination) == k:
                result.append(combination.copy())
                return

            if num <= n: 
                combination.append(num)
                backtrack(num + 1)
                combination.pop()
                backtrack(num + 1)


        backtrack(1)
        return result