class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        result = 0

        for num in numsSet:
            if num - 1 not in numsSet:
                curr = num
                count = 1
                while curr + 1 in numsSet:
                    count += 1
                    curr += 1

                result = max(result, count)
        
        return result