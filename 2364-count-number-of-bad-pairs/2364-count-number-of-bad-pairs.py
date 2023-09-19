class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        numsLength = len(nums)
        countDict = defaultdict(int)
        for i in range(numsLength):
            nums[i] -= i
            countDict[nums[i]] += 1
        
        count = 0
        for key in countDict:
            count += math.comb(countDict[key], 2)
        return math.comb(numsLength, 2) - count