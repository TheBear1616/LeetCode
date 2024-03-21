class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort()
        low = 0
        high = len(nums) - 1

        while low <= high:
            if abs(nums[low]) < abs(nums[high]):
                high -= 1
            else:
                low += 1
        
        return nums[high]