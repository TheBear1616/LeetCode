class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1

        idx = 0
        totalSurplus = 0
        
        for i in range(len(gas)):
            totalSurplus += gas[i] - cost[i]
            if totalSurplus < 0:
                idx = i + 1
                totalSurplus = 0

        return idx if totalSurplus >= 0 else -1