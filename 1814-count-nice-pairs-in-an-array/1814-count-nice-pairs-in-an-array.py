class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        def rev(num):
            numStr = str(num)[::-1]
            return int(numStr) if numStr[0] != 0 else  int(numStr[1:])
        
        freqDict = collections.defaultdict(int)
        for idx, num in enumerate(nums):
            nums[idx] -= rev(nums[idx])
            freqDict[nums[idx]] += 1
        
        count = 0
        for key in freqDict:
            count = (count + math.comb(freqDict[key], 2)) % MOD

        return count
