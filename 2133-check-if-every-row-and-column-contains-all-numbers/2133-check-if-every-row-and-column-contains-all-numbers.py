class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if (
                    matrix[r][c] in rows[r]
                    or matrix[r][c] in cols[c]
                ):
                    return False
                cols[c].add(matrix[r][c])
                rows[r].add(matrix[r][c])

        return True