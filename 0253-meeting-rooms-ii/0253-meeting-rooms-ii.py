class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        minHeap = [intervals[0][1]]

        for interval in intervals[1:]:
            if minHeap and minHeap[0] <= interval[0]:
                heapq.heappop(minHeap)

            heapq.heappush(minHeap, interval[1])                
            
        return len(minHeap)