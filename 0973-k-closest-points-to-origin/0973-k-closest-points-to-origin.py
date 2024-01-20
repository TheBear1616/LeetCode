class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for point in points:
            x, y = point
            distance = math.sqrt((x * x) + (y * y))
            heapq.heappush(minHeap, (-distance, point))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return [point for distance, point in minHeap]