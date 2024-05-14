class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.extend([-9e9, 9e9])
        heaters.sort()
        houses.sort()
        diff = 1e9
        res = 0
        i = 0

        for house in houses:
            while house > heaters[i + 1]:
                i += 1
            diff = min(abs(house - heaters[i]), abs(house - heaters[i + 1]))
            res = max(res, diff)

        return res