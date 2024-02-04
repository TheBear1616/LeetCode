class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        wSum = 0
        wStart = 0
        result = 1e9

        for wEnd in range(len(nums)):
            wSum += nums[wEnd]
            while wSum >= target:
                result = min(result, wEnd - wStart + 1)
                wSum -= nums[wStart]
                wStart += 1
        
        return result if result != 1e9 else 0
