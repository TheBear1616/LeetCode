class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums) - 1 
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[end]:
                end -= 1
            if nums[mid] == nums[start]:
                start += 1
            elif nums[start] < nums[mid]:
                if  nums[start] <= target < nums[mid]:
                    end = mid - 1
                else: 
                    start = mid + 1
            else:
                if  nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return False