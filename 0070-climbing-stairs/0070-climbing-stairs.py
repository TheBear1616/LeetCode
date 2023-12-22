class Solution:
    def climbStairs(self, n: int) -> int:
        firstStep = secondStep = 1

        while n-1:
            firstStep, secondStep = firstStep + secondStep, firstStep
            n -= 1
        
        return firstStep