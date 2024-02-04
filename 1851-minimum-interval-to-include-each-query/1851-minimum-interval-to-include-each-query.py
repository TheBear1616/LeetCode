class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []
        i = 0
        result = {}

        for query in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]
                heapq.heappush(minHeap, (end - start + 1, end))
                i += 1
            
            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)
            
            result[query] = minHeap[0][0] if minHeap else -1
        
        return [result[q] for q in queries]