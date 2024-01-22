class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid1), len(grid1[0])
        visit = set()

        def dfs(r, c):
            if ( r < 0 or c < 0 or r == ROWS or c == COLS or grid2[r][c] == 0 or (r, c) in visit):
                return True
            
            visit.add((r, c))
            result = False if grid1[r][c] == 0 else True
            result = dfs(r+1, c) and result
            result = dfs(r-1, c) and result
            result = dfs(r, c+1) and result
            result = dfs(r, c-1) and result
            
            return result
        
        subIslands = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] and (r,c) not in visit and dfs(r, c):
                    subIslands += 1
        
        return subIslands