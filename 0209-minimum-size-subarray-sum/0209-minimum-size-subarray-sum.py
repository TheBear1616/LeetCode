class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        wStart = 0
        minSubArrayLen = 1e9
        currSum = 0

        for wEnd, num in enumerate(nums):
            currSum += num
            while (currSum >= target):
                minSubArrayLen = min(minSubArrayLen, wEnd - wStart + 1)
                currSum -= nums[wStart]
                wStart += 1

        return 0 if minSubArrayLen == 1e9 else minSubArrayLen