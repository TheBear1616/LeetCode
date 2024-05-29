class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)
        if (totalSum + target) < 0 or (totalSum + target) % 2 != 0: return 0
        
        newTarget = (totalSum + target) // 2
        if newTarget < 0: return 0
        
        dp = [[0 for _ in range(newTarget + 1)] for _ in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            dp[i][0] = 1

        for i in range(1, len(nums) + 1):
            for j in range(1, newTarget + 1):
                if nums[i-1] > j or nums[i-1] == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j - nums[i-1]]

        zero_count = nums.count(0)
        
        return (2 ** zero_count) * dp[-1][newTarget]
