class Solution:
    def canJump(self, nums: List[int]) -> bool:
        steps = 1

        for i in range(len(nums)-2,-1,-1):
            steps = 1 if nums[i] >= steps else steps + 1
        
        return True if steps == 1 else False
