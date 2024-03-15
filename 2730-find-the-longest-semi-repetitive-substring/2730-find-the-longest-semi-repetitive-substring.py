class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        wStart = 0
        prevRepIdx = 0
        ans = 0
        prev = s[0]

        for wEnd in range(len(s)):
            if s[wEnd] == prev:
                if prevRepIdx:
                    wStart = prevRepIdx
                prevRepIdx = wEnd
            ans = max(ans, wEnd - wStart + 1)
            prev = s[wEnd]
        
        return ans
