class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = collections.deque([])
        time = 0
        freshOranges = 0
        directions= [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    freshOranges += 1
                elif grid[i][j] == 2:
                    que.append((i, j))
        
        while que and freshOranges > 0:
            qLEn = len(que)
            for _ in range(qLEn):
                r, c = que.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 1:
                        grid[row][col] = 2
                        que.append((row, col))
                        freshOranges -= 1

            time += 1
        
        return time if freshOranges == 0 else -1
