class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        n = len(timeSeries)        
        total = 0

        for i in range(n - 1):
            total += min(timeSeries[i + 1] - timeSeries[i], duration)
            
        return total + duration