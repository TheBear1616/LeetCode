class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqWords = collections.Counter(words)
        freqHeap = []

        for word, freq in freqWords.items():
            heapq.heappush(freqHeap, [-freq, word])

        return [heapq.heappop(freqHeap)[1] for _ in range(k)]