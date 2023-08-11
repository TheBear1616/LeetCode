class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        low = 0
        high = (row * col) - 1
        while low <= high:
            mid = (low + high) // 2
            midRow = mid // col
            midCol = mid % col
            if target == matrix[midRow][midCol]:
                return True
            elif target > matrix[midRow][midCol]:
                low = mid + 1
            else:
                high = mid - 1
        
        return False