class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strList = s.split()
        if len(pattern) != len(strList):
            return False

        strDict = {}
        patternDict = {}

        for pat, word in zip(pattern, strList):
            if (pat in patternDict and patternDict[pat] != word) or (word in strDict and strDict[word] != pat):
                return False
            
            patternDict[pat] = word
            strDict[word] = pat
        
        return True