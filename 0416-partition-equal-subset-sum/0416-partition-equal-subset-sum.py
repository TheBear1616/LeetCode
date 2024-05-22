class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 == 1: return False

        target = totalSum // 2
        dp = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]

        for i in range(len(nums) + 1):
            dp[i][0] = True

        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[len(nums)][target]
