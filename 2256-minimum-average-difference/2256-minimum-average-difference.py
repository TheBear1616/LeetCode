class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        leftSum = 0
        leftLength = 0
        totalSum = sum(nums)
        totalLength = len(nums)
        minAvgDiff = (1e9, 0)
        nums.append(0)
        
        for i in range(len(nums)-1):
            leftSum += nums[i]
            leftLength += 1
            totalSum -= nums[i]
            totalLength -= 1

            if totalLength == 0: totalLength += 1

            minAvgDiff = min(minAvgDiff, (abs((leftSum // leftLength) - (totalSum // totalLength)), i))

        return minAvgDiff[1]