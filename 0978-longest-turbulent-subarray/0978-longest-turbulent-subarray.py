class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        wStart = 0
        wEnd = 1
        res = 1
        prev = ""

        while wEnd < len(arr):
            if arr[wEnd - 1] > arr[wEnd] and prev != ">":
                res = max(res, wEnd - wStart + 1)
                wEnd += 1
                prev = ">"
            elif arr[wEnd - 1] < arr[wEnd] and prev != "<":
                res = max(res, wEnd - wStart + 1)
                wEnd += 1
                prev = "<"
            else:
                wEnd = wEnd + 1 if arr[wEnd - 1] == arr[wEnd] else wEnd
                wStart = wEnd - 1
                prev = ""
        
        return res