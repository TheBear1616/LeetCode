class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        currEnd = points[0][1]
        count = 1

        for start, end in points[1:]:
            if start > currEnd:
                count += 1
                currEnd = end
        
        return count