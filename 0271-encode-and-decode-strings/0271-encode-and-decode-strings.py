class Codec:
    strDict = {}
    def encode(self, strs: List[str]) -> str:
        key = ""
        for word in strs:
            if len(word) > 0:
                key += str(len(word)) + word[0]
        
        self.strDict[key] = strs 
        return key
        
    def decode(self, s: str) -> List[str]:
        return self.strDict[s]
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))