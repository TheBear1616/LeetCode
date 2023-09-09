class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        maxOnesLength = 0
        binary = {0: 0}
        
        for end in range(len(nums)):
            if nums[end] == 0: binary[0] += 1
            while binary[0] == k+1:
                if nums[start] == 0: binary[0] -= 1
                start += 1
            
            maxOnesLength = max(end - start + 1, maxOnesLength)
        
        return maxOnesLength