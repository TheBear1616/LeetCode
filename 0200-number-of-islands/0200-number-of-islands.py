class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == "1":
                    self.countNunumIslands(grid, i, j)
                    result += 1
        
        return result
        
    def countNunumIslands(self, grid, row, col):
        if row > -1 and row < len(grid) and col > -1 and col < len(grid[0]) and  grid[row][col] == "1":
            grid[row][col] = -1
            self.countNunumIslands(grid, row-1, col)
            self.countNunumIslands(grid, row+1, col)
            self.countNunumIslands(grid, row, col-1)
            self.countNunumIslands(grid, row, col+1)    