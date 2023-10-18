class Codec:
    def __init__(self):
        self.encodeMap = {}
        self.decodeMap = {}
        self.baseURL = "http://tinyurl.com/"
    
    def encode(self, longURL: str) -> str:
        if longURL not in self.encodeMap:
            shortURL = self.baseURL + str(len(self.encodeMap) + 1)
            self.encodeMap[longURL] = shortURL
            self.decodeMap[shortURL] = longURL
        return self.encodeMap[longURL]

    def decode(self, shortURL: str) -> str:
        return self.decodeMap[shortURL]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))