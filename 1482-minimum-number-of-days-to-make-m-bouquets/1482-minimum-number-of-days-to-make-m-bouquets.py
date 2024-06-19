class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def getNumOfBouquets(mid):
            count = 0
            ans = 0

            for bloom in bloomDay:
                if bloom <= mid:
                    count += 1
                else:
                    count = 0
                    
                if count == k:
                    ans += 1
                    count = 0
            
            return ans
        
        if (m * k) > len(bloomDay): return -1
        left = min(bloomDay)
        right = max(bloomDay)
        result = -1

        while left <= right:
            mid = left + ((right - left) // 2)
            if getNumOfBouquets(mid) >= m:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result