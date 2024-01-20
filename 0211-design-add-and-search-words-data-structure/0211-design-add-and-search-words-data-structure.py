class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        currNode = self.root

        for char in word:
            if char not in currNode.children:
                currNode.children[char] = TrieNode()
            currNode = currNode.children[char]
        
        currNode.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(idx, root):
            currNode = root

            for i in range(idx, len(word)):
                char = word[i]
                if char == ".":
                    for child in currNode.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if char not in currNode.children:
                        return False
                    currNode = currNode.children[char]

            return currNode.endOfWord
        
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)