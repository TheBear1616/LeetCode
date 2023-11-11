class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        currSum = 0
        prefixSums = {0: -1}

        for i, num in enumerate(nums):
            currSum += num
            remainder = currSum % k
            if remainder not in prefixSums:
                prefixSums[remainder] = i
            elif i - prefixSums[remainder] > 1:
                return True
        
        return False