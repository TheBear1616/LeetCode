class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = collections.deque()
        freshOranges = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    freshOranges += 1
                if grid[r][c] == 2:
                    que.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while freshOranges > 0 and que:
            length = len(que)
            for i in range(length):
                r, c = que.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        que.append((row, col))
                        freshOranges -= 1
            time += 1
        return time if freshOranges == 0 else -1