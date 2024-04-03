class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)

        for wStart in range(n - m + 1):
            for i in range(m):
                if needle[i] != haystack[wStart + i]:
                    break
                if i == m - 1:
                    return wStart

        return -1