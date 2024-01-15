class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        res = 1e9

        def canShip(capacity):
            ships, currCapacity = 1, capacity
            for weight in weights:
                if currCapacity - weight < 0:
                    ships += 1
                    currCapacity = capacity
                
                currCapacity -= weight

            return ships <= days

        while left <= right:
            mid = (left + right) // 2
            if canShip(mid):
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return res
