class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        low, high = 2, x // 2
        while (low <= high):
            mid = int((low + high) // 2)
            if mid ** 2 < x:
                low = mid + 1
            elif mid ** 2 > x:
                high = mid - 1
            else:
                return mid

        return high
