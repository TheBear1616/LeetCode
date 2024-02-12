class TrieNode:

    def __init__(self):
        self.endOfWord = False
        self.children = {}
    
    def addWord(self, word):
        currNode = self
        for char in word:
            if char not in currNode.children:
                currNode.children[char] = TrieNode()
            currNode = currNode.children[char]
        currNode.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        ROWS = len(board)
        COLS = len(board[0])
        result = set()
        visited = set()

        def dfs(row, col, word, currNode):
            if (row < 0 or col < 0 or row >= ROWS or col >= COLS or
                (row, col) in visited or board[row][col] not in currNode.children): return 
            
            visited.add((row, col))

            currNode = currNode.children[board[row][col]]
            word += board[row][col]
            if currNode.endOfWord:
                result.add(word)
            
            dfs(row + 1, col, word, currNode)
            dfs(row - 1, col, word, currNode)
            dfs(row, col + 1, word, currNode)
            dfs(row, col - 1, word, currNode)

            visited.remove((row, col))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, "", root)
        
        return list(result)
