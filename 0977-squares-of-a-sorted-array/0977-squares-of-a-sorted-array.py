class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [None] * len(nums)
        left, right = 0, len(nums) - 1
        for idx in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[idx] = nums[left] ** 2
                left += 1
            else:
                result[idx] = nums[right] ** 2
                right -= 1
        
        return result