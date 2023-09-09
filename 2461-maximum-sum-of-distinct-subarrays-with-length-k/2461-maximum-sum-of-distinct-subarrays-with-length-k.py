class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        start = 0
        result = 0
        wSum = 0
        numsSet = set()

        for end in range(len(nums)):
            while (len(numsSet) >= k) or (nums[end] in numsSet):
                numsSet.remove(nums[start])
                wSum -= nums[start]
                start += 1

            numsSet.add(nums[end])
            wSum += nums[end]
            if (end - start + 1) == k: result = max(result, wSum)
        
        return result
