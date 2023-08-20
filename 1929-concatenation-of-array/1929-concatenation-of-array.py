class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [None] * 2 * n
        for idx in range(n):
            result[idx] = result[idx+n] = nums[idx]
        
        return result