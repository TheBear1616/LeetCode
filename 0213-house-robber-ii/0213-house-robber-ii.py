class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            nums = [0,0] + nums
            n = len(nums)
            for i in range(2, n):
                nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
            
            return nums[n - 1]

        return max(nums[0], helper(nums[1:]), helper(nums[:-1])) 
        
        