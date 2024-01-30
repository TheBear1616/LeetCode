class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [1e9] * (amount + 1)
        dp[0] = 0

        for amt in range(1, amount + 1):
            for coin in coins:
                if amt - coin >= 0:
                    dp[amt] = min(1 + dp[amt - coin], dp[amt])

        return dp[amount] if dp[amount] != 1e9 else -1