class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        maxEle = -1e9
        maxEleIdx = -1
        minEle = 1e9
        minEleIdx = -1
        swaps = 0

        for i in range(len(nums)):
            if nums[i] >= maxEle:
                maxEle = nums[i]
                maxEleIdx = i

        for i in range(maxEleIdx, len(nums) - 1):
            nums[i], nums[i+1] = nums[i+1], nums[i]
            swaps += 1
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] <= minEle:
                minEle = nums[i]
                minEleIdx = i
        
        for i in range(minEleIdx, 0, -1):
            nums[i], nums[i-1] = nums[i-1], nums[i]
            swaps += 1

        return swaps