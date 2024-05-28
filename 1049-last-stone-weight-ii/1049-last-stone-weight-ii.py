class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totalSum = sum(stones)
        possibleSumVals = self.subSet(stones, totalSum // 2)
        result = totalSum

        for i in range(len(possibleSumVals)):
            if possibleSumVals[i]:
                result = min(result, totalSum - (2 * i))
        
        return result

    
    def subSet(self, stones, targetSum):
        dp = [[False for _ in range(targetSum + 1)] for _ in range(len(stones) + 1)]

        for i in range(len(stones) + 1):
            dp[i][0] = True
        
        for i in range(1, len(stones) + 1):
            for j in range(1, targetSum + 1):
                if stones[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - stones[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[-1]