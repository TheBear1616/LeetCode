class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        refBoard = copy.deepcopy(board)
        def nextGeneration(i, j):
            currentSum = 0

            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for dir in directions:
                new_i, new_j = i + dir[0], j + dir[1]
                if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]):
                    currentSum += refBoard[new_i][new_j]

            if refBoard[i][j] == 1 and (currentSum < 2 or currentSum > 3):
                board[i][j] = 0
            elif refBoard[i][j] == 0 and currentSum == 3:
                board[i][j] = 1
            

        for i in range(len(board)):
            for j in range(len(board[0])):
                nextGeneration(i, j)
