class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        currSum = 0
        prefixSums = collections.defaultdict(int)
        prefixSums[0] = 1
        result = 0

        for num in nums:
            currSum += num
            multiple = currSum % k
            result += prefixSums[multiple]
            prefixSums[multiple] += 1
        
        return result