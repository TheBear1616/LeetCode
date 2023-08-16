class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        usedRooms = 0
        startTimings = sorted(i[0] for i in intervals)
        endTimings = sorted(i[1] for i in intervals)
        start = 0
        end = 0

        while start < len(intervals):
            if startTimings[start] >= endTimings[end]:
                usedRooms -= 1
                end += 1
            
            usedRooms += 1
            start += 1
        
        return usedRooms