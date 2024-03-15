class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        nums = [(interval[0], idx) for idx, interval in enumerate(intervals)]
        nums.sort()
        result = []

        def binarySearch(target):
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid][0] == target:
                    return nums[mid][1]
                elif nums[mid][0] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            
            return nums[low][1] if low < len(nums) else -1

        for start, end in intervals:
            result.append(binarySearch(end))
        
        return result