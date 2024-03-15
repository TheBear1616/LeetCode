class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort()
        pointsSet = set([tuple(point) for point in points])

        result = 1e9

        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points[i + 1: ]):
                if x1 < x2 and y1 < y2 and (x1, y2) in pointsSet and (x2, y1) in pointsSet:
                    area = (x2 - x1) * (y2 - y1)
                    result = min(area, result)

        return result if result != 1e9 else 0