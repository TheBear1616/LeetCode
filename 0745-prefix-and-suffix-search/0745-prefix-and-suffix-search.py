class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.wordIdx = -1
    
    def addWord(self, word, idx):
        currNode = self
        for char in word:
            if char not in currNode.children:
                currNode.children[char] = TrieNode()
            currNode = currNode.children[char]
            currNode.wordIdx = idx
        currNode.endOfWord = True
        
class WordFilter:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for idx, word in enumerate(words):
            for i in range(len(word)-1, -1, -1):
                self.root.addWord(word[i:] + "#" + word, idx)

    def f(self, pref: str, suff: str) -> int:
        currNode = self.root
        for char in suff + "#" + pref:
            if char not in currNode.children:
                return -1
            currNode = currNode.children[char]
        return currNode.wordIdx
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)