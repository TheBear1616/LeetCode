class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        leftMin = [nums[0]] * len(nums)
        rightMin = [nums[-1]] * len(nums)
        minSum = 1e9

        for i in range(1,len(nums)):
            leftMin[i] = min(leftMin[i-1], nums[i])

        for i in range(len(nums)-2, -1, -1):
            rightMin[i] = min(rightMin[i+1], nums[i])
        
        for i in range(1, len(nums) - 1):
            if leftMin[i - 1] < nums[i] > rightMin[i + 1]:
                minSum = min(minSum, leftMin[i - 1] + nums[i] + rightMin[i + 1])
        
        return minSum if minSum != 1e9 else -1
