class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if (
                (mid - 1 < 0 or nums[mid - 1] != nums[mid]) and
                (mid + 1 >= len(nums) or nums[mid + 1] != nums[mid])
            ):
                return nums[mid]
            
            pivot = mid if nums[mid + 1] == nums[mid] else mid - 1

            if pivot % 2 == 1:
                high = mid - 1
            else:
                low = mid + 1
