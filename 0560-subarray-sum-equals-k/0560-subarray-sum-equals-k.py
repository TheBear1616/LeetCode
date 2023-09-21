class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        currSum = 0
        prefixSums = collections.defaultdict(int)
        prefixSums[0] = 1

        for num in nums:
            currSum += num
            diff = currSum - k

            result += prefixSums[diff]
            prefixSums[currSum] += 1        
        
        return result