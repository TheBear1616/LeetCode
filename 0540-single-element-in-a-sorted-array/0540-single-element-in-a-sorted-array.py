class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)
            if (
                (mid - 1 < 0 or nums[mid - 1] != nums[mid]) and 
                (mid + 1 == len(nums) or nums[mid + 1] != nums[mid])
            ):
                return nums[mid]
            
            leftSize = mid - 1 if nums[mid - 1] == nums[mid] else mid

            if leftSize % 2 == 0:
                left = mid + 1
            else:
                right = mid - 1
