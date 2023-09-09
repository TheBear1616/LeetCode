class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        start = 0
        charDict = {}
        maxSubstring = 0

        for end in range(len(s)):
            charDict[s[end]] = 1 + charDict.get(s[end], 0)
            while len(charDict) > k:
                charDict[s[start]] -= 1
                if charDict[s[start]] == 0: del charDict[s[start]]
                start += 1

            maxSubstring = max(maxSubstring, end - start + 1)

        return maxSubstring