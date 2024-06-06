class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        while count:
            minVal = min(count)
            for val in range(minVal, minVal + groupSize):
                if count[val] == 0: return False
                count[val] -= 1
                if count[val] == 0:
                    del count[val]
        
        return True
