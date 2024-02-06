class Solution:
    def findMin(self, nums: List[int]) -> int:     
        ans = nums[0]   
        low = 0
        high = len(nums) - 1

        while low <= high:
            if nums[low] < nums[high]:
                ans = min(ans, nums[low])
                break
            
            mid = (low + high) // 2
            ans = min(ans, nums[mid])
            if nums[low] <= nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return ans