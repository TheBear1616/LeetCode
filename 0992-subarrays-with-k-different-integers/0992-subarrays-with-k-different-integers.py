class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        left = 0
        mid = 0
        result = 0
        numsCount = defaultdict(int)

        for right in range(len(nums)):
            numsCount[nums[right]] += 1

            while len(numsCount) > k:
                numsCount[nums[mid]] -= 1
                if numsCount[nums[mid]] == 0:
                    del numsCount[nums[mid]]
                mid += 1
                left = mid
            
            while numsCount[nums[mid]] > 1:
                numsCount[nums[mid]] -= 1
                mid += 1

            if len(numsCount) == k:
                result += mid - left + 1

        return result