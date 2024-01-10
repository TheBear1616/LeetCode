class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqEle = collections.Counter(nums)
        minHeap = []
        
        for key, value in freqEle.items():
            heapq.heappush(minHeap, (value, key))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return [ key for value, key in minHeap ]