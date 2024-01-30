class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        currMax = 1
        currMin = 1
        result = nums[0]

        for num in nums:
            oldMax = currMax
            currMax = max(num, num * oldMax, num * currMin)
            currMin = min(num, num * oldMax, num * currMin)

            result = max(result, currMax)
        
        return result