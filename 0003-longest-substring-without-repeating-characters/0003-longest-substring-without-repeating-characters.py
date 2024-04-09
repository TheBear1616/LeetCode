class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        wStart = 0
        ans = 0
        charSet = set()

        for wEnd in range(len(s)):
            while s[wEnd] in charSet:
                charSet.remove(s[wStart])
                wStart += 1
            
            charSet.add(s[wEnd])
            ans = max(ans, wEnd - wStart + 1)
        
        return ans