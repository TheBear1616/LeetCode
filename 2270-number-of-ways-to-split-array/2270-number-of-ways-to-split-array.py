class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        leftSum = 0
        totalSum = sum(nums)
        count = 0

        for i in range(len(nums)-1):
            leftSum += nums[i]
            totalSum -= nums[i]
            count += 1 if leftSum >= totalSum else 0
        
        return count
