class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        newInterval = intervals[0]
        result = []

        for i in range(1, len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                newInterval = intervals[i]
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        
        result.append(newInterval)
        return result