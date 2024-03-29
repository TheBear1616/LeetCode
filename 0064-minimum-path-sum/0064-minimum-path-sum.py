class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}

        def dfs(row, col):
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return grid[row][col]

            if row >= len(grid) or col >= len(grid[0]):
                return int(1e9)
            
            if (row, col) in dp:
                return dp[(row, col)]
            
            dp[(row, col)] = grid[row][col] + min(dfs(row + 1, col), dfs(row, col + 1))

            return dp[(row, col)]
        
        return dfs(0, 0)
