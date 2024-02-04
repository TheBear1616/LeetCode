class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1

        while left <= right:
            if right - left + 1 == k:
                return arr[left:right + 1]
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                right -= 1
            else:
                left += 1
        