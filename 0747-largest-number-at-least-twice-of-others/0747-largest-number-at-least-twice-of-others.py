class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        indexDict = {ele: idx for idx, ele in enumerate(nums)}
        nums.sort()
        return indexDict[nums[-1]] if nums[-2] * 2 <= nums[-1] else -1