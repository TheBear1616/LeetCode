class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        minSum = 1e9
        minLeft = [nums[0]] * len(nums)
        minRight = [nums[-1]] * len(nums)

        for i in range(1, len(nums)):
            minLeft[i] = min( minLeft[i-1], nums[i])
        for i in range(len(nums)-2, -1, -1):
            minRight[i] = min(minRight[i+1], nums[i])

        for i in range(1, len(nums)-1):
            if minLeft[i-1] < nums[i] > minRight[i+1]:
                minSum = min(minSum, minLeft[i-1] + nums[i] + minRight[i+1])
        
        return minSum if minSum != 1e9 else -1