class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    maxArea = max(maxArea, self.dfs(grid, row, col))
        
        return maxArea

    def dfs(self, grid, row, col) -> int:
        currArea = 0
        if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == 1:
            grid[row][col] = -1
            currArea = 1
            currArea += self.dfs(grid, row-1, col)
            currArea += self.dfs(grid, row+1, col)
            currArea += self.dfs(grid, row, col-1)
            currArea += self.dfs(grid, row, col+1)

        return currArea