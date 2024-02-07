class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        result = []

        for spell in spells:
            start = 0
            end = len(potions) - 1
            mid = 0
            while start <= end:
                mid = (start + end) // 2
                if spell * potions[mid] < success:
                    start = mid + 1
                else:
                    end = mid - 1
            
            result.append(len(potions) - start)
        
        return result
