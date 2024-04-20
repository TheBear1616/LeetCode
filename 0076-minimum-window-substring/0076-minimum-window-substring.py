class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return t

        res = [-1, -1]
        resLen = 1e9
        wStart = 0

        tMap = collections.Counter(t)
        currMap = collections.defaultdict(int)

        have = 0
        need = len(tMap)

        for wEnd in range(len(s)):
            currMap[s[wEnd]] += 1

            if s[wEnd] in tMap and currMap[s[wEnd]] == tMap[s[wEnd]]:
                have += 1

            while have == need:
                if (wEnd - wStart + 1) < resLen:
                    resLen = (wEnd - wStart + 1)
                    res = [wStart, wEnd]
                
                currMap[s[wStart]] -= 1
                if s[wStart] in tMap and currMap[s[wStart]] < tMap[s[wStart]]:
                    have -= 1
                
                wStart += 1
            
        return s[res[0] : res[1] + 1] if resLen != 1e9 else ""