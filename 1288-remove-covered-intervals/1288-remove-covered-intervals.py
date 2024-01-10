class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        result = [intervals[0]]

        for interval in intervals[1:]:
            if result[-1][0] <= interval[0] and interval[1] <= result[-1][1]:
                continue
            
            result.append(interval)

        return len(result)