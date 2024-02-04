class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.triplets = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.findTriplets(nums, -nums[i], i+1)
        
        return self.triplets
            
    def findTriplets(self, nums, target, left):
        right = len(nums) - 1
        while left < right:
            currSum = nums[left] + nums[right]
            if target == currSum:
                self.triplets.append([-target, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif target < currSum:
                right -= 1
            else:
                left += 1