class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()
        result = 0
        currEnd = int(-1e9)

        for start, end in nums:
            if start > currEnd:
                result += end - start + 1
            elif end > currEnd:
                result += end - currEnd

            currEnd = max(currEnd, end)
        
        return result
