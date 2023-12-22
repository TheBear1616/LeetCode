class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        N = len(nums)

        rob1, rob2 = nums[N - 1], 0
        
        for i in range(N - 2, -1, -1):
            rob1, rob2 = max(rob2 + nums[i], rob1), rob1

        
        return rob1