class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        visit = set()

        def dfs(row, col, value):
            if (
                row < 0
                or col < 0
                or row == ROWS
                or col == COLS
                or image[row][col] != value
                or (row, col) in visit
            ):
                return
            
            visit.add((row, col))
            image[row][col] = color
            dfs(row + 1, col, value)
            dfs(row - 1, col, value)
            dfs(row, col + 1, value)
            dfs(row, col - 1, value)

        for r in range(ROWS):
            for c in range(COLS):
                if r == sr and c == sc:
                    dfs(r, c, image[r][c])
        
        return image