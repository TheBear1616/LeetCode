class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -1e9
        wSum = 0

        for wEnd in range(len(nums)):
            wSum = max(nums[wEnd], wSum + nums[wEnd])
            maxSum = max(maxSum, wSum)
        
        return maxSum
