class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        numSubArrays = 0

        for num in nums:
            if num == 0:
                numSubArrays += 1
            else:
                numSubArrays = 0
            result += numSubArrays

        return result