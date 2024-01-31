class Solution:
    def jump(self, nums: List[int]) -> int:
        left, right = 0, 0
        minJump = 0

        while right < len(nums) - 1:
            maxJump = 0
            for idx in range(left, right + 1):
                maxJump = max(maxJump, idx + nums[idx])
            left = right + 1
            right = maxJump
            minJump += 1
        
        return minJump