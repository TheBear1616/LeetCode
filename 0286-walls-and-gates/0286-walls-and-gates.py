class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        que = collections.deque()
        ROWS = len(rooms)
        COLS = len(rooms[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    que.append((r, c))
        
        while que:
            queLength = len(que)
            for _ in range(queLength):
                r, c = que.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (
                        row in range(ROWS)
                        and col in range(COLS)
                        and rooms[row][col] == 2147483647
                    ):
                        rooms[row][col] = 1 + rooms[r][c]
                        que.append((row, col))
        
        return