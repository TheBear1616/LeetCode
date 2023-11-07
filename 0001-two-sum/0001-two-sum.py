class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dSum = {}

        for i, num in enumerate(nums):
            if target - num in dSum:
                return [dSum[target - num], i]
            
            dSum[num] = i