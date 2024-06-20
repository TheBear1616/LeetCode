class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits), key=lambda x: x[0])
        max_heap = []
        n = len(projects)
        i = 0
        
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
            if max_heap:
                w += -heapq.heappop(max_heap)
            else:
                break
                
        return w
