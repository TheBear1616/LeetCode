class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        wStart = 0
        wEnd = 0
        wSum = 0
        result = 0

        while wEnd < len(nums):
            wSum += nums[wEnd]

            while (nums[wEnd] * (wEnd - wStart + 1)) > wSum + k:
                wSum -= nums[wStart]
                wStart += 1
            
            result = max(result, (wEnd - wStart + 1))
            wEnd += 1
        
        return result