class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
            
        low = 2
        high = x // 2

        while low <= high:
            mid = (low + high) // 2
            sqrNum = mid * mid
            if sqrNum == x:
                return mid
            elif sqrNum > x:
                high = mid - 1
            else:
                low = mid + 1
         
        return high