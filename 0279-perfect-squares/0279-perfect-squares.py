class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0

        for target in range(1, n + 1):
            for num in range(1, target + 1):
                nSqr = num * num
                if target - nSqr < 0: break
                dp[target] = min(dp[target], 1 + dp[target - nSqr])

        return dp[n]