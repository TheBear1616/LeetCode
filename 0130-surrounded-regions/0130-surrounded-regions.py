class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        visit = set()
        
        def dfs(r, c, visit):
            if ( r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or board[r][c] == "X"
                or (r, c) in visit
            ):
                return
            
            visit.add((r,c))
            dfs(r + 1, c, visit)
            dfs(r - 1, c, visit)
            dfs(r, c + 1, visit)
            dfs(r, c - 1, visit)
        
        for c in range(COLS):
            dfs(0, c, visit)
            dfs(ROWS - 1, c, visit)
        
        for r in range(ROWS):
            dfs(r, 0, visit)
            dfs(r, COLS - 1, visit)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in visit:
                    board[r][c] = "X"
        