class TrieNode:

    def __init__(self):
        self.endOfWord = False
        self.children = {}
    
    def addWords(self, words):
        for word in words:
            currNode = self
            for char in word:
                if char not in currNode.children:
                    currNode.children[char] = TrieNode()
                currNode = currNode.children[char]
            currNode.endOfWord = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = TrieNode()
        root.addWords(dictionary)
        dp = {len(s): 0}

        def dfs(i):
            if i in dp: return dp[i]

            res = 1 + dfs(i + 1)
            currNode = root
            for j in range(i, len(s)):
                if s[j] not in currNode.children:
                    break
                currNode = currNode.children[s[j]]
                if currNode.endOfWord:
                    res = min(res, dfs(j + 1))
            dp[i] = res
            return res
        
        return dfs(0)