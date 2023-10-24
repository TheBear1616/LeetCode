class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        result = 0
        num = x

        while x > 0:
            result = (result * 10) + x % 10 
            x = x // 10

        return result == num