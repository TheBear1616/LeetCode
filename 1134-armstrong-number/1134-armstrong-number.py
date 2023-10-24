class Solution:
    def isArmstrong(self, n: int) -> bool:
        result = 0
        numStr = str(n)
        power = len(numStr)

        for ch in numStr:
            result += pow(int(ch), power)
        
        return n == result
