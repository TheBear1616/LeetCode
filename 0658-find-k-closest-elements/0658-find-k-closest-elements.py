class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low = 0
        high = len(arr) - 1

        while low <= high:
            if high - low + 1 == k:
                return arr[low: high + 1]
            elif abs(arr[low] - x) <= abs(arr[high] - x):
                high -= 1
            else:
                low += 1
        