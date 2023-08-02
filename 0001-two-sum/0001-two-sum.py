class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dSum = {}
        for idx, ele in enumerate(nums):
            if target - ele in dSum:
                return [idx, dSum[target-ele]]
            else:
                dSum[ele] = idx