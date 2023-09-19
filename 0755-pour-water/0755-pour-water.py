class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        while volume:
            toFill = k
            currHeight = heights[k]

            left = k - 1
            while left >= 0:
                if heights[left] > currHeight:
                    break
                if heights[left] < currHeight:
                    toFill = left
                    currHeight = heights[left]
                left -= 1
            
            if toFill == k:
                right = k + 1
                while right < len(heights) :
                    if heights[right] > currHeight:
                        break
                    if heights[right] < currHeight:
                        toFill = right
                        currHeight = heights[right]
                    right += 1
            
            heights[toFill] += 1
            volume -= 1
        
        return heights