class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0
        j = 0
        lastMatch = -1
        star = -1

        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == "?"):
                i += 1
                j += 1
            elif j < len(p) and p[j] == "*":
                lastMatch = i
                star = j
                j += 1
            elif star != -1:
                i = lastMatch + 1
                j = star + 1
                lastMatch += 1
            else:
                return False

        while j < len(p) and p[j] == "*":
            j += 1
        
        return j == len(p)