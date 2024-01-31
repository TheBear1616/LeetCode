class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        wStart = 0
        wEnd = 1
        result = 1
        prevSign = ""

        while wEnd < len(arr):
            if arr[wEnd - 1] > arr[wEnd] and prevSign != ">":
                prevSign = ">"
                result = max(result, wEnd - wStart + 1)
                wEnd += 1
            elif arr[wEnd - 1] < arr[wEnd] and prevSign != "<":
                prevSign = "<"
                result = max(result, wEnd - wStart + 1)
                wEnd += 1
            else:
                wEnd = wEnd + 1 if arr[wEnd - 1] == arr[wEnd] else wEnd
                wStart = wEnd - 1
                prevSign = ""
        
        return result