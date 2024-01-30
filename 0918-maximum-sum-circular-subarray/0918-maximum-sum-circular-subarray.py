class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax, globalMin = nums[0], nums[0]
        currMax, currMin = nums[0], nums[0]
        total = nums[0]
        for num in nums[1:]:
            currMax = max(currMax + num, num)
            currMin = min(currMin + num, num)
            total += num
            globalMax = max(globalMax, currMax)
            globalMin = min(globalMin, currMin)
        
        return max(globalMax, total - globalMin) if globalMax > 0 else globalMax