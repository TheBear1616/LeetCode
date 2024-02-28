class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        maxTime = neededTime[0]
        sumTime = neededTime[0]

        for i in range(1, len(colors)):
            if colors[i] != colors[i - 1]:
                time += (sumTime - maxTime)
                maxTime = -1
                sumTime = 0    
            
            sumTime += neededTime[i]
            maxTime = max(maxTime, neededTime[i])
        
        time += (sumTime - maxTime)
        return time 