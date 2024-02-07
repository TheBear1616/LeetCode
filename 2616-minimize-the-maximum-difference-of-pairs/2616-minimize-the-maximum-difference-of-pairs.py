class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)

        def countValidPair(threshold):
            i, count = 0, 0
            while i < n - 1:
                if abs(nums[i] - nums[i + 1]) <= threshold:
                    count += 1
                    i += 1
                i += 1
            
            return count
        
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2
            if countValidPair(mid) >= p:
                right = mid
            else:
                left = mid + 1
        
        return left
