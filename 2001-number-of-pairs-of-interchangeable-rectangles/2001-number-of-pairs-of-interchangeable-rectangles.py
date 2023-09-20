class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        rectRatios = [ rect[0] / rect[1] for rect in rectangles ]
        freqDict = collections.Counter(rectRatios)

        count = 0
        for key in freqDict:
            count += math.comb(freqDict[key], 2)
        
        return count