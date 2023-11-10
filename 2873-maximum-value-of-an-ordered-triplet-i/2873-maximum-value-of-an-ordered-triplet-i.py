class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxVal = 0
        maxLeft = [nums[0]] * len(nums)
        maxRight = [nums[-1]] * len(nums)

        for i in range(1, len(nums)):
            maxLeft[i] = max(maxLeft[i-1], nums[i])
        for i in range(len(nums)-2, -1, -1):
            maxRight[i] = max(maxRight[i+1], nums[i])

        for i in range(1, len(nums)-1):
            maxVal = max(maxVal, (maxLeft[i-1] - nums[i]) * maxRight[i+1])
        
        return maxVal