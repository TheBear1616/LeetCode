class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        nonGrumpySum = 0

        for i in range(len(customers)):
            if grumpy[i] == 0: nonGrumpySum += customers[i]

        wStart = 0
        wSum = 0
        maxGrumpySum = 0

        for wEnd in range(len(customers)):
            wSum += customers[wEnd] * grumpy[wEnd]
            if (wEnd - wStart + 1) == minutes:
                maxGrumpySum = max(maxGrumpySum, wSum)
                wSum -= customers[wStart] * grumpy[wStart]
                wStart += 1

        return nonGrumpySum + maxGrumpySum
