class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(idx, comb, total):
            if total == target:
                result.append(comb.copy())
                return
            
            prev = -1
            for i in range(idx, len(candidates)):
                if candidates[i] == prev:
                    continue
                
                comb.append(candidates[i])
                if total + candidates[i] <= target: backtrack(i + 1, comb, total + candidates[i])
                comb.pop()
                prev = candidates[i]
        
        backtrack(0, [], 0)
        return result
