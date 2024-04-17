class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        sqr = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                value = board[i][j]

                if value == ".":
                    continue
                    
                if value in row[i] or value in col[j] or value in sqr[(i // 3, j // 3)]:
                    return False
                
                row[i].add(value)
                col[j].add(value)
                sqr[(i // 3, j // 3)].add(value)
        
        return True