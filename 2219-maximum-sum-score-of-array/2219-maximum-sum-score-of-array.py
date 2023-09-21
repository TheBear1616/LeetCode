class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        currSum = 0
        result = -1e9
        
        for num in nums:
            currSum += num
            result = max(result, max(currSum, totalSum))
            totalSum -= num
        
        return result