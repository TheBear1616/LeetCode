class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        revNum = int(str(num)[::-1])
        secRevNum = int(str(revNum)[::-1])

        return num == secRevNum