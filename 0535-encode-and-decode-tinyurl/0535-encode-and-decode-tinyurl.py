class Codec:

    def __init__(self):
        self.encodeMap = {}
        self.decodeMap = {}
        self.baseURL = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.encodeMap:
            shortUrl = self.baseURL + str(len(self.encodeMap) + 1)
            self.encodeMap[longUrl] = shortUrl
            self.decodeMap[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        return self.decodeMap[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))