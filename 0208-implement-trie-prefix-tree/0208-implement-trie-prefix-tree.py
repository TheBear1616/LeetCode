class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
            currentNode = currentNode.children[char]
        
        currentNode.endOfWord = True

    def search(self, word: str) -> bool:
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                return False
            currentNode = currentNode.children[char]
        
        return currentNode.endOfWord

    def startsWith(self, prefix: str) -> bool:
        currentNode = self.root
        for char in prefix:
            if char not in currentNode.children:
                return False
            currentNode = currentNode.children[char]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)