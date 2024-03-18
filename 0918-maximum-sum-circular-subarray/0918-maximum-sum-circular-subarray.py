class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax, globalMin = -1e9, 1e9
        currMax, currMin = 0, 0
        totalSum = 0

        for num in nums:
            totalSum += num
            currMax = max(num, num + currMax)
            globalMax = max(currMax, globalMax)
            currMin = min(num, num + currMin)
            globalMin = min(currMin, globalMin)
        
        return globalMax if globalMax < 0 else max(totalSum - globalMin, globalMax)