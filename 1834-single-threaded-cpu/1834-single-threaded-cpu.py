class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for idx, task in enumerate(tasks):
            task.append(idx)
        
        tasks.sort(key = lambda t: t[0])
        minHeap = []
        result = []
        i = 0
        time = tasks[0][0]

        while minHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minHeap, (tasks[i][1], tasks[i][2]))
                i += 1
            
            if not minHeap:
                time = tasks[i][0]
            else:
                procTime, idx = heapq.heappop(minHeap)
                time += procTime
                result.append(idx)

        return result
        