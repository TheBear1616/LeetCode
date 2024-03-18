class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1 or num == 0:
            return True
        
        low = 2
        high = num // 2

        while low <= high:
            mid = (low + high) // 2
            sqrNum = mid * mid
            if sqrNum == num:
                return True
            elif sqrNum > num:
                high = mid - 1
            else:
                low = mid + 1

        return False