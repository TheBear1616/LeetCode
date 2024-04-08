class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums, target, True)

        if left == -1:
            return [-1, -1]
        
        return [left, self.binarySearch(nums, target, False)]
    
    def binarySearch(self, nums, target, firstIdx):
        idx = -1
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] == target:
                if firstIdx:
                    high = mid - 1
                else:
                    low = mid + 1
                    
                idx = mid
        
        return idx        