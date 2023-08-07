class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsSet = set(nums)
        return True if len(nums) > len(numsSet) else False 
        