class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            pivotIdx = (left + right) // 2
            pivotEle = matrix[pivotIdx // len(matrix[0])][pivotIdx % len(matrix[0])]
            if target == pivotEle:
                return True
            elif target > pivotEle:
                left = pivotIdx + 1
            else:
                right = pivotIdx - 1
        
        return False