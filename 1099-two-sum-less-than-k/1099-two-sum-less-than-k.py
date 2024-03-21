class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return -1 

        nums.sort()
        ans = -1
        low = 0
        high = len(nums) - 1

        while low < high:
            if nums[low] + nums[high] < k:
                ans = max(ans, nums[low] + nums[high])
                low += 1
            else:
                high -= 1
    
        return ans
