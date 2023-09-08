class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort()
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            if end > intervals[i][0]:
                end = min(end, intervals[i][1])
                count += 1
            else:
                end = intervals[i][1]

        return count