class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.quadruplets = set()
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.threeSum(nums[i+1:], target - nums[i], nums[i])

        return [list(quadruplet) for quadruplet in self.quadruplets]
    
    def threeSum(self, nums, target, firstNum):
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                currSum = nums[i] + nums[left] + nums[right]
                if currSum == target:
                    self.quadruplets.add((firstNum, nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif currSum > target:
                    right -= 1
                else:
                    left += 1