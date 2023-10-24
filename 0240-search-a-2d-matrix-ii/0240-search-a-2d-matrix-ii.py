class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numRows, numCols = len(matrix), len(matrix[0])
        row, col = numRows - 1, 0

        while row >= 0 and col < numCols:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            else:
                col += 1
        
        return False