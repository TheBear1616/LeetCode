class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dSum = collections.defaultdict(int)

        for idx, num in enumerate(nums):
            if target - num in dSum:
                return [dSum[target - num], idx]
            
            dSum[num] = idx