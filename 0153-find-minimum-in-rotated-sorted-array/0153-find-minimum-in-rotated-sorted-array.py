class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[left] <= nums[mid] and nums[mid] >= nums[right]:
                if nums[mid] > nums[mid+1]:
                    return nums[mid+1]
                left = mid + 1
            elif nums[left] >= nums[mid] and nums[mid] <= nums[right]:
                if nums[mid-1] > nums[mid]:
                    return nums[mid]
                right = mid - 1
            else:
                right = mid - 1
        
        return nums[left]
                