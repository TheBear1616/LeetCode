class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.wordFound = False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j] and not self.wordFound:
                    self.dfs(board, i, j, word, 0)
    
        return self.wordFound

    
    def dfs(self, board, row, col, word, idx):
        if row >= 0 and row < len(board) and col >= 0 and col < len(board[0]) and board[row][col] == word[idx]:

            temp = board[row][col]
            board[row][col] = '#'
            
            if idx == len(word)-1:
                self.wordFound = True
                return

            self.dfs(board, row - 1, col, word, idx + 1)
            self.dfs(board, row + 1, col, word, idx + 1)
            self.dfs(board, row, col - 1, word, idx + 1)
            self.dfs(board, row, col + 1, word, idx + 1)
            board[row][col] = temp
