class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        combination = []

        def backtrack(idx, total):
            if total == target:
                result.append(combination.copy())
                return

            if idx >= len(candidates) or total > target:
                return
            
            combination.append(candidates[idx])
            backtrack(idx, total + candidates[idx])
            combination.pop()
            backtrack(idx + 1, total)
        
        backtrack(0, 0)
        return result