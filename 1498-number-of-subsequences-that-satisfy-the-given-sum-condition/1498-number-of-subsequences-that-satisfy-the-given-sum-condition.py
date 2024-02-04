class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        right = len(nums) - 1
        res = 0
        mod = (10 ** 9 + 7)

        for idx, left in enumerate(nums):
            while left + nums[right] > target and idx <= right:
                right -= 1
            if idx <= right:
                res += 2 ** (right - idx)
                res %= mod
        
        return res