class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(math.sqrt(c))

        while left <= right:
            currSum = (left * left) + (right * right)
            if currSum == c:
                return True
            if currSum < c:
                left += 1
            else:
                right -= 1
                
        return False
        