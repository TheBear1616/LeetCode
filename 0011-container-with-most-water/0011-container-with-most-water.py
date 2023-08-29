class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = 0

        while left < right:
            length = height[right] if height[left] > height[right] else height[left]
            breadth = right - left
            area = max(area, length * breadth)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return area
