class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -1 * num)

        if self.maxHeap and self.minHeap and (-1 * self.maxHeap[0]) > self.minHeap[0]:
            value = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -1 * value)
        
        if len(self.maxHeap) > len(self.minHeap) + 1:
            value = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -1 * value)
        
        if len(self.minHeap) > len(self.maxHeap) + 1:
            value = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1 * value)

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -1 * self.maxHeap[0]
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        
        return ((-1 * self.maxHeap[0]) + self.minHeap[0]) / 2
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()