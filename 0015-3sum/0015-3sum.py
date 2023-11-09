class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.triplets = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.searchTriplet(nums, -nums[i], i+1)
            
        return self.triplets
    
    def searchTriplet(self, nums, target, left):
        right = len(nums)-1
        while left < right:
            currentSum = nums[left] + nums[right]
            if target == currentSum:
                self.triplets.append([-target, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -=1 
            elif target > currentSum:
                left += 1
            else:
                right -= 1