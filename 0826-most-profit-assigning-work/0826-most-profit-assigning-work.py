class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort()
        tasks = sorted(zip(difficulty, profit), key=lambda x: x[0])
        tasks.append((1e9, 0))
        prevProfit = 0
        idx = 0
        result = 0

        for difficulty, profit in tasks:
            while idx < len(worker) and worker[idx] < difficulty:
                result += prevProfit
                idx += 1

            prevProfit = max(prevProfit, profit)

        return result