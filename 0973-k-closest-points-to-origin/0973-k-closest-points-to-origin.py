class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closestPoint = []

        for idx, point in enumerate(points):
            eDistance = self.euclideanDistance(point) * -1
            heapq.heappush(closestPoint, [eDistance, idx])
            if len(closestPoint) > k:
                heapq.heappop(closestPoint)
        
        return [points[point[1]] for point in closestPoint]
    
    def euclideanDistance(self, point):
        x, y = point
        return math.sqrt((x * x) + (y * y))