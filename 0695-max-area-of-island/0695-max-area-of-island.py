class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, self.dfs(grid, r, c))

        return maxArea
    
    def dfs(self, grid, r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0 or grid[r][c] == -1:
            return 0

        area = 1
        grid[r][c] = -1
        area += self.dfs(grid, r - 1, c)
        area += self.dfs(grid, r + 1, c)
        area += self.dfs(grid, r, c - 1)
        area += self.dfs(grid, r, c + 1)

        return area