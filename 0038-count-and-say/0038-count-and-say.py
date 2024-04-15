class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        sayStr = self.countAndSay(n - 1)

        return self.say(sayStr)
    
    def say(self, sayStr):
        sayStr += "0"
        count = 1
        res = ""
        for i in range(len(sayStr) - 1):
            if sayStr[i] == sayStr[i+1]:
                count += 1
            else:
                res += str(count) + sayStr[i]
                count = 1

        return res