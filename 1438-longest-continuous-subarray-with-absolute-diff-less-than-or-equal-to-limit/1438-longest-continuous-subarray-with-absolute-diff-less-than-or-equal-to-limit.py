class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        minHeap = []
        maxHeap = []
        maxLen = 1

        for right in range(len(nums)):
            heapq.heappush(minHeap, (nums[right], right))
            heapq.heappush(maxHeap, (-nums[right], right))

            while minHeap[0][1] < left:
                heapq.heappop(minHeap)
            while maxHeap[0][1] < left:
                heapq.heappop(maxHeap)
            
            if -maxHeap[0][0] - minHeap[0][0] <= limit:
                maxLen = max(maxLen, right - left + 1)
            else:
                left += 1

        return maxLen