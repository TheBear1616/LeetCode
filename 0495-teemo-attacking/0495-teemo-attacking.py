class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        result = [[timeSeries[0], timeSeries[0] + duration - 1]]
        ans = 0

        for time in timeSeries[1:]:
            if result[-1][-1] >= time:
                result[-1][-1] = max(result[-1][-1], time + duration - 1)
            else:
                result.append([time, time + duration - 1])
        
        for [start, end] in result:
            ans += end - start + 1

        return ans