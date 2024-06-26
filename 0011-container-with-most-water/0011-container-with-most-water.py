class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        result = 0

        while left < right:
            length = min(height[left], height[right])
            width = right - left

            result = max(result, length * width)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return result