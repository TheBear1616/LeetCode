class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        curr_flips = 0
        result = 0
        n = len(nums)

        for i in range(n):
            if i - k >= 0 and nums[i - k] == 2:
                curr_flips -= 1
            if (nums[i] + curr_flips) % 2 == 0:
                if i + k > n: return -1
                result += 1
                curr_flips += 1
                nums[i] = 2

        return result