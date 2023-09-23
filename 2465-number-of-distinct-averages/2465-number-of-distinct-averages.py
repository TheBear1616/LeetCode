class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        numDistAvgs = set()
        left = 0
        right = len(nums) - 1
        nums.sort()

        while left < right:
            numDistAvgs.add((nums[left] + nums[right]) / 2)
            left += 1
            right -= 1
        
        return len(numDistAvgs)
        