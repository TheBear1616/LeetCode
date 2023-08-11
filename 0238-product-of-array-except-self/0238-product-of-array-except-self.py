class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        identity = 1

        for i in range(len(nums)):
            result[i] = identity
            identity *= nums[i]
        
        identity = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= identity
            identity *= nums[i]

        return result