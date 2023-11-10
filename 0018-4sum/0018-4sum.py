class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.quadruplets = set()
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.threeSum(nums[i+1:], target - nums[i], nums[i])
        
        return [list(quadruplet) for quadruplet in self.quadruplets]

    def threeSum(self, nums: List[int], target: int, first_num: int):
        for j in range(len(nums)):
            if j > 0 and nums[j] == nums[j - 1]:
                continue
            left, right = j + 1, len(nums) - 1
            while left < right:
                current_sum = nums[j] + nums[left] + nums[right]
                if current_sum == target:
                    self.quadruplets.add((first_num, nums[j], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
