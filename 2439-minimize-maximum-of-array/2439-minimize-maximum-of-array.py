class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        totalSum = 0
        result = 0
        for i in range(len(nums)):
            totalSum += nums[i]
            result = max(result, math.ceil(totalSum / (i + 1)))
        return int(result)