class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        maxEle = -1e9
        maxEleIdx = -1
        minEle = 1e9
        minEleIdx = -1

        for i in range(len(nums)):
            if nums[i] >= maxEle:
                maxEle = nums[i]
                maxEleIdx = i
            if nums[i] < minEle:
                minEle = nums[i]
                minEleIdx = i

        swaps = minEleIdx + (len(nums) - 1 - maxEleIdx)

        return swaps - 1 if minEleIdx > maxEleIdx else swaps
