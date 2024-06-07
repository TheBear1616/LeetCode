class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def longestCommonSubsequence(text1: str, text2: str) -> str:
            n = len(text1)
            m = len(text2)
            result = [["" for _ in range(m + 1)] for _ in range(n + 1)]

            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if text1[i - 1] == text2[j - 1]: 
                        result[i][j] = result[i - 1][j - 1] + text1[i - 1]
                    else:
                        result[i][j] = result[i - 1][j] if len(result[i - 1][j]) > len(result[i][j - 1]) else result[i][j - 1]
            
            return result[n][m]
        
        lcs = longestCommonSubsequence(str1, str2)
        i = 0
        j = 0
        result = ""

        for ch in lcs:
            while str1[i] != ch:
                result += str1[i]
                i += 1

            while str2[j] != ch:
                result += str2[j]
                j += 1

            result += ch
            i += 1
            j += 1

        result += str1[i:] + str2[j:]
        return result